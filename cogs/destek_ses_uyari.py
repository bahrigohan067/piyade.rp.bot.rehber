# -*- coding: utf-8 -*-
import os
import asyncio
import discord
from discord.ext import commands, tasks
from discord import app_commands
from datetime import datetime, timezone, timedelta

from config import (
    GUILD_ID, DESTEK_BEKLEME_SES_ID, KURUCU_ROL_ID, kurucu_mu,
    MESAI_SES_DOSYASI, BEKLEME_MUZIKLERI,
    get_ffmpeg_executable, mesai_ici_mi, mesai_disi_mi,
    SUNUCU_ADI, RENK_ANA, RENK_TURUNCU, RENK_YESIL
)

def yetkili_mi(member: discord.Member) -> bool:
    """Kullanıcının @|👤KURUCU yetkisine sahip olup olmadığını denetler."""
    return kurucu_mu(member)


class DestekSesUyari(commands.Cog):
    """
    Piyade RP — 7/24 Kesintisiz Destek Bekleme Ses Yöneticisi:
    
    1. Mesai İçi Saatler (12:00 Öğlen - 01:00 Gece):
       - Bot kanalda kalır ve bekleme müziklerini (bekleme_muzik_1 & bekleme_muzik_2)
         sürekli olarak döngü halinde (loop) çalar.
         
    2. Mesai Dışı Saatler (01:00 Gece - 12:00 Öğlen):
       - Bot kanaldan hiç ayrılmaz.
       - Kanalda insan yokken sessizce nöbette bekler.
       - Odaya bir üye girdiğinde mesai dışı sesli uyarısını oynatır.
       - Üye çıkmadığı sürece her 15 saniyede bir bu uyarıyı tekrarlar.
    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self._baglanma_kilit = asyncio.Lock()
        self._gecikme_gorevi: asyncio.Task | None = None
        self.main_task: asyncio.Task | None = None
        self.member_joined_event = asyncio.Event()
        self.test_mode_override: str | None = None  # None, 'mesai_ici', 'mesai_disi'
        self.current_track_index = 0
        self.active_playing_type = "Beklemede"

    async def cog_load(self):
        # Arka plan bağlantı ve ses denetim döngüsünü başlat
        self.voice_supervisor.start()

    def cog_unload(self):
        self.voice_supervisor.cancel()
        if self._gecikme_gorevi and not self._gecikme_gorevi.done():
            self._gecikme_gorevi.cancel()
        if self.main_task and not self.main_task.done():
            self.main_task.cancel()

    # =========================================================================
    # YARDIMCI METOTLAR
    # =========================================================================

    def get_turkiye_saati(self) -> datetime:
        """Türkiye saati (UTC+3) ile güncel zamanı döndürür."""
        tz_tr = timezone(timedelta(hours=3))
        return datetime.now(tz_tr)

    def kanaldaki_insan_sayisi(self, channel: discord.VoiceChannel) -> int:
        """Kanalda bulunan bot olmayan gerçek üye sayısını hesaplar."""
        if not channel:
            return 0
        return len([m for m in channel.members if not m.bot])

    def get_aktif_mesai_durumu(self) -> bool:
        """
        True: Mesai içi (12:00 - 01:00) -> Müzik modu
        False: Mesai dışı (01:00 - 12:00) -> Uyarı modu
        """
        if self.test_mode_override == "mesai_ici":
            return True
        elif self.test_mode_override == "mesai_disi":
            return False
        return mesai_ici_mi()

    async def _ses_kanalina_baglan(self) -> discord.VoiceClient | None:
        """
        Botun hedef ses kanalında (DESTEK_BEKLEME_SES_ID) kesintisiz bağlı kalmasını sağlar.
        Kilit (Lock) mekanizması ile birden fazla bağlantı çağrısının çakışmasını (çık-gir yapmasını) önler.
        """
        async with self._baglanma_kilit:
            guild = self.bot.get_guild(GUILD_ID)
            if not guild:
                return None

            channel = guild.get_channel(DESTEK_BEKLEME_SES_ID)
            if not channel or not isinstance(channel, discord.VoiceChannel):
                return None

            vc = guild.voice_client

            # 1. Zaten hedef kanalda bağlı ve aktifse dokunma!
            if vc and vc.is_connected():
                if vc.channel and vc.channel.id == DESTEK_BEKLEME_SES_ID:
                    return vc
                # Başka kanala çekildiyse hedef kanala geri taşı
                try:
                    await vc.move_to(channel)
                    print(f"[SES] 🔄 Bot hedef ses kanalına taşındı: {channel.name}", flush=True)
                    return vc
                except Exception as e:
                    print(f"[SES HATA] Kanal taşıma hatası: {e}", flush=True)

            # 2. Bağlantı yoksa veya kopmuşsa temizce bağlan
            try:
                if vc:
                    try:
                        await vc.disconnect(force=True)
                    except Exception:
                        pass
                vc = await channel.connect(reconnect=True, self_deaf=True)
                print(f"[SES] 🔌 Bot 7/24 ses kanalına bağlandı: {channel.name} ({channel.id})", flush=True)
                return vc
            except Exception as e:
                print(f"[SES HATA] Kanala bağlanırken hata: {e}", flush=True)
                return None

    def _tetikle_gecikmeli_baglan(self, saniye: int = 5):
        """Kopma anında spam bağlantıyı önlemek için gecikmeli bağlantı kurar."""
        if self._gecikme_gorevi and not self._gecikme_gorevi.done():
            self._gecikme_gorevi.cancel()

        async def _bekle_ve_baglan():
            try:
                await asyncio.sleep(saniye)
                await self._ses_kanalina_baglan()
            except asyncio.CancelledError:
                pass

        self._gecikme_gorevi = asyncio.create_task(_bekle_ve_baglan())

    # =========================================================================
    # KESİNTİSİZ 7/24 SES KONTROL DÖNGÜSÜ
    # =========================================================================

    async def _audio_controller_loop(self, channel: discord.VoiceChannel):
        """
        Botun ses kanalında kesintisiz olarak saat kontrolü yapmasını,
        mesai içi müziklerini ve mesai dışı tekrarlayan uyarılarını yöneten çekirdek döngü.
        """
        ffmpeg_bin = get_ffmpeg_executable()
        guild = channel.guild
        print(f"[SES] 🚀 Kesintisiz Ses Denetim Döngüsü Devrede. Hedef Kanal: {channel.name}", flush=True)

        while True:
            try:
                vc = guild.voice_client
                # Bot henüz ses kanalına bağlı değilse veya kopmuşsa bağlantıyı bekle (connect çağırma, bekçi halletsin)
                if not vc or not vc.is_connected() or not vc.channel or vc.channel.id != channel.id:
                    await asyncio.sleep(2)
                    continue

                mesai_aktif = self.get_aktif_mesai_durumu()

                # -------------------------------------------------------------
                # DURUM A: MESAİ İÇİ (12:00 - 01:00) ➡️ SÜREKLİ BEKLEME MÜZİĞİ
                # -------------------------------------------------------------
                if mesai_aktif:
                    self.active_playing_type = "Bekleme Müziği (Mesai İçi)"
                    parca_yolu = BEKLEME_MUZIKLERI[self.current_track_index % len(BEKLEME_MUZIKLERI)]

                    if not os.path.exists(parca_yolu):
                        print(f"[SES HATA] Müzik dosyası bulunamadı: {parca_yolu}", flush=True)
                        await asyncio.sleep(5)
                        continue

                    # Sesi başlat
                    try:
                        if vc.is_playing():
                            vc.stop()
                        source = discord.PCMVolumeTransformer(
                            discord.FFmpegPCMAudio(parca_yolu, executable=ffmpeg_bin, options="-vn"),
                            volume=0.5
                        )
                        vc.play(source)
                        print(f"[SES] 🎵 [Mesai İçi] Çalıyor: Parça #{self.current_track_index + 1} ({os.path.basename(parca_yolu)})", flush=True)
                    except Exception as e:
                        print(f"[SES HATA] Müzik başlatma hatası: {e}", flush=True)
                        await asyncio.sleep(3)
                        continue

                    # Parça çalarken 1 saniyelik aralıklarla kontrol et
                    while vc.is_connected() and vc.is_playing():
                        # Saat 01:00 olduysa müziği durdur
                        if not self.get_aktif_mesai_durumu():
                            print("[SES] ⏰ Saat 01:00 oldu! Mesai içi bekleme müziği durduruluyor.", flush=True)
                            vc.stop()
                            break
                        await asyncio.sleep(1)

                    self.current_track_index = (self.current_track_index + 1) % len(BEKLEME_MUZIKLERI)
                    await asyncio.sleep(1)

                # -------------------------------------------------------------
                # DURUM B: MESAİ DIŞI (01:00 - 12:00) ➡️ 15 SANİYEDE BİR SESLİ UYARI
                # -------------------------------------------------------------
                else:
                    self.active_playing_type = "Mesai Dışı Uyarı Modu"
                    insan_sayisi = self.kanaldaki_insan_sayisi(channel)

                    # Kanalda insan yoksa sessizce bekle
                    if insan_sayisi == 0:
                        try:
                            await asyncio.wait_for(self.member_joined_event.wait(), timeout=3.0)
                            self.member_joined_event.clear()
                        except asyncio.TimeoutError:
                            pass
                        continue

                    if not os.path.exists(MESAI_SES_DOSYASI):
                        print(f"[SES HATA] Mesai dışı ses dosyası eksik: {MESAI_SES_DOSYASI}", flush=True)
                        await asyncio.sleep(5)
                        continue

                    try:
                        if vc.is_playing():
                            vc.stop()
                        source = discord.PCMVolumeTransformer(
                            discord.FFmpegPCMAudio(MESAI_SES_DOSYASI, executable=ffmpeg_bin, options="-vn"),
                            volume=1.0
                        )
                        vc.play(source)
                        print(f"[SES] 📢 [Mesai Dışı] Uyarı sesi oynatılıyor... (Kanalda {insan_sayisi} üye var)", flush=True)
                    except Exception as e:
                        print(f"[SES HATA] Uyarı sesi başlatma hatası: {e}", flush=True)
                        await asyncio.sleep(3)
                        continue

                    # Ses çalımı bitene kadar bekle
                    while vc.is_connected() and vc.is_playing():
                        if self.kanaldaki_insan_sayisi(channel) == 0:
                            vc.stop()
                            break
                        if self.get_aktif_mesai_durumu():
                            vc.stop()
                            break
                        await asyncio.sleep(0.5)

                    if self.kanaldaki_insan_sayisi(channel) == 0:
                        print("[SES] ℹ️ Kanal boşaldı, uyarı durdu. Bot kanalda nöbette.", flush=True)
                        continue

                    print("[SES] ⏳ Uyarı tamamlandı. 15 saniyelik bekleme başladı...", flush=True)
                    for _ in range(15):
                        await asyncio.sleep(1)
                        if self.kanaldaki_insan_sayisi(channel) == 0 or self.get_aktif_mesai_durumu():
                            break

            except asyncio.CancelledError:
                break
            except Exception as e:
                print(f"[SES BEKLENMEDİK HATA] Ses döngüsünde istisna: {e}", flush=True)
                await asyncio.sleep(5)

    # =========================================================================
    # EVENT LİSTENER: on_voice_state_update
    # =========================================================================

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        """
        Destek kanalına bir üye girdiğinde veya bot kazara atıldığında tetiklenir.
        """
        # 1. Eğer botun kendisi ise:
        if member.id == self.bot.user.id:
            # Bot hedef kanalda değilse veya bağlantısı koptuysa 5 saniye gecikmeyle bağlan
            if not after.channel or after.channel.id != DESTEK_BEKLEME_SES_ID:
                print("[SES UYARI] ⚠️ Bot ses kanalından ayrıldı veya taşındı! 5 saniye sonra yeniden bağlanacak...", flush=True)
                self._tetikle_gecikmeli_baglan(5)
            return

        if member.bot:
            return

        # 2. Gerçek bir üye Destek Bekleme kanalına katıldıysa
        if after.channel and after.channel.id == DESTEK_BEKLEME_SES_ID:
            print(f"[SES] 👤 {member.display_name} destek bekleme ses kanalına katıldı.", flush=True)
            self.member_joined_event.set()

    # =========================================================================
    # SÜREKLİ GÖZETMEN (SUPERVISOR LOOP)
    # =========================================================================

    @tasks.loop(seconds=30)
    async def voice_supervisor(self):
        """
        Botun her zaman ses kanalında kalmasını ve ana oynatma görevinin
        kesintisiz çalışmasını denetleyen gözetmen.
        """
        if not self.bot.is_ready():
            return

        guild = self.bot.get_guild(GUILD_ID)
        if not guild:
            return

        channel = guild.get_channel(DESTEK_BEKLEME_SES_ID)
        if not channel or not isinstance(channel, discord.VoiceChannel):
            return

        # 1. Bot bağlı değilse veya kanalda değilse bağla
        vc = guild.voice_client
        if not vc or not vc.is_connected() or not vc.channel or vc.channel.id != channel.id:
            await self._ses_kanalina_baglan()

        # 2. Ana ses döngüsü task'ı çalışmıyorsa başlat
        if self.main_task is None or self.main_task.done():
            self.main_task = asyncio.create_task(self._audio_controller_loop(channel))

    @voice_supervisor.before_loop
    async def before_voice_supervisor(self):
        try:
            await self.bot.wait_until_ready()
            await self._ses_kanalina_baglan()
        except (RuntimeError, Exception):
            pass


    # =========================================================================
    # YÖNETİM KOMUTLARI: /mesai-ses-durum & /mesai-ses-mod
    # =========================================================================

    @app_commands.command(
        name="mesai-ses-durum",
        description="Destek ses kanalı canlı durumunu, çalan parçayı ve mesai bilgisini gösterir."
    )
    async def cmd_mesai_durum(self, interaction: discord.Interaction):
        if not yetkili_mi(interaction.user):
            await interaction.response.send_message(
                f"❌ Bu yönetim komutunu yalnızca **KURUCU** (<@&{KURUCU_ROL_ID}>) kullanabilir.",
                ephemeral=True
            )
            return

        guild = interaction.guild or self.bot.get_guild(GUILD_ID)
        channel = guild.get_channel(DESTEK_BEKLEME_SES_ID)
        insan_sayisi = self.kanaldaki_insan_sayisi(channel) if channel else 0
        suan = self.get_turkiye_saati().strftime("%d.%m.%Y %H:%M:%S")

        mesai_ici = self.get_aktif_mesai_durumu()
        durum_metin = "🟢 **Mesai İçi (12:00 - 01:00)** — Sürekli Bekleme Müziği Aktif" if mesai_ici else "🔴 **Mesai Dışı (01:00 - 12:00)** — Otomatik 15sn Sesli Uyarı Devrede"

        voice_client = guild.voice_client
        baglanti_durumu = "🟢 Kanala Bağlı & 7/24 Aktif" if (voice_client and voice_client.is_connected()) else "🔴 Bağlı Değil (Bağlanılıyor...)"

        parca_1_var = os.path.exists(BEKLEME_MUZIKLERI[0])
        parca_2_var = os.path.exists(BEKLEME_MUZIKLERI[1])
        uyari_var = os.path.exists(MESAI_SES_DOSYASI)

        override_bilgi = f"`{self.test_mode_override}`" if self.test_mode_override else "`Otomatik (Saate Göre)`"

        embed = discord.Embed(
            title="🎙️ 7/24 Destek Ses Kanalı ve Mesai Kontrol Merkezi",
            description=(
                f"**Türkiye Saati:** `{suan}`\n"
                f"**Mesai Durumu:** {durum_metin}\n"
                f"**Çalışma Modu:** {override_bilgi}\n\n"
                f"────────────────────────────────────────\n\n"
                f"• **Hedef Ses Kanalı:** <#{DESTEK_BEKLEME_SES_ID}>\n"
                f"• **Bot Bağlantı Statüsü:** {baglanti_durumu}\n"
                f"• **Şu Anki Eylem:** `{self.active_playing_type}`\n"
                f"• **Kanalda Bekleyen Üye:** `{insan_sayisi} Kişi`\n\n"
                f"────────────────────────────────────────\n\n"
                f"📁 **Ses Dosyaları Durumu:**\n"
                f"• 🎵 Bekleme Müziği 1: `{'✅ Yüklü' if parca_1_var else '❌ Eksik'}`\n"
                f"• 🎵 Bekleme Müziği 2: `{'✅ Yüklü' if parca_2_var else '❌ Eksik'}`\n"
                f"• 📢 Mesai Dışı Uyarı: `{'✅ Yüklü' if uyari_var else '❌ Eksik'}`\n\n"
                f"⏰ **Mesai Saatleri Kuralı:**\n"
                f"• **12:00 - 01:00:** Müzik 1 & 2 sürekli döngüde çalar.\n"
                f"• **01:00 - 12:00:** Üye varken her 15 saniyede bir uyarı sesi tekrarlanır."
            ),
            color=RENK_YESIL if mesai_ici else RENK_TURUNCU
        )
        embed.set_footer(text=f"{SUNUCU_ADI} • 7/24 Kesintisiz Ses Sistemi")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(
        name="mesai-ses-mod",
        description="Destek ses kanalının çalışma modunu test amacıyla manuel olarak ayarlar veya otomatiğe alır."
    )
    @app_commands.describe(
        mod="Seçilecek çalışma modu (Otomatik saat, Zorunlu Mesai İçi Müzik veya Zorunlu Mesai Dışı Uyarı)"
    )
    @app_commands.choices(mod=[
        app_commands.Choice(name="Otomatik (Gerçek Türkiye Saatine Göre)", value="otomatik"),
        app_commands.Choice(name="Test: Zorunlu Mesai İçi (Sürekli Müzik Çalar)", value="mesai_ici"),
        app_commands.Choice(name="Test: Zorunlu Mesai Dışı (15sn Sesli Uyarı)", value="mesai_disi"),
    ])
    async def cmd_mesai_mod(self, interaction: discord.Interaction, mod: str):
        if not yetkili_mi(interaction.user):
            await interaction.response.send_message(
                f"❌ Bu yönetim komutunu yalnızca **KURUCU** (<@&{KURUCU_ROL_ID}>) kullanabilir.",
                ephemeral=True
            )
            return

        if mod == "otomatik":
            self.test_mode_override = None
            mesaj = "✅ Ses sistemi **Otomatik Türkiye Saati** moduna alındı. (12:00-01:00 Müzik, 01:00-12:00 Uyarı)."
        elif mod == "mesai_ici":
            self.test_mode_override = "mesai_ici"
            mesaj = "🎵 Ses sistemi test için **Zorunlu Mesai İçi Müzik Moduna** alındı. Parçalar sürekli döngüde çalacaktır."
        else:
            self.test_mode_override = "mesai_disi"
            mesaj = "📢 Ses sistemi test için **Zorunlu Mesai Dışı Uyarı Moduna** alındı. Kanalda biri olduğunda 15 saniyede bir uyarı sesi çalacaktır."

        # Çalan müziği kesip yeni modu anında uygulasın
        guild = interaction.guild or self.bot.get_guild(GUILD_ID)
        voice_client = guild.voice_client
        if voice_client and voice_client.is_playing():
            voice_client.stop()

        self.member_joined_event.set()
        await interaction.response.send_message(mesaj, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(DestekSesUyari(bot))
