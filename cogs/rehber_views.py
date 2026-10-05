# -*- coding: utf-8 -*-
import os
import aiohttp
import discord
from discord.ui import View, Select, Button
from datetime import datetime

from config import (
    SUNUCU_ADI, ERLC_SUNUCU_KODU, ROBLOX_GRUP_LINK,
    GUILD_ID, ANA_BOT_ID, ERLC_API_KEY,
    REHBER_PANEL_KANAL_ID, TICKET_KANAL_LINK,
    RP_DUYURU_KANAL_ID, RP_OYLAMA_KANAL_ID,
    BANNER_PATH,
    RENK_ANA, RENK_ALTIN, RENK_YESIL, RENK_KIRMIZI, RENK_MOR, RENK_TURUNCU, RENK_KOYU
)
from data.rehber_data import (
    DIVIDER,
    ANASAYFA_METIN, KANALLAR_METIN, TUM_KURALLAR_METIN,
    RP_TERIMLERI_METIN, KAYIT_SISTEMI_METIN, CETE_SISTEMI_METIN,
    VS_TALEP_METIN, ERLC_BILGI_METIN, DIGER_METIN
)

FOOTER_TEXT = f"{SUNUCU_ADI} • Resmi Sunucu Rehberi"


# =====================================================================
# CANLI ER:LC VE ANA BOT BİLGİSİ ÇEKİCİ
# =====================================================================

async def get_live_erlc_info(bot: discord.Client) -> str:
    guild = bot.get_guild(GUILD_ID)
    status_lines = []

    # 1. Ana botun (<@1544144846875267253>) Presence / Activity'sini oku
    if guild:
        main_bot = guild.get_member(ANA_BOT_ID)
        if main_bot:
            durumlar = []
            for act in main_bot.activities:
                if act and hasattr(act, 'name') and act.name:
                    durumlar.append(f"• `{act.name}`")
            if durumlar:
                status_lines.append(f"🤖 **Ana Bot ({main_bot.mention}) Canlı Durumu:**\n" + "\n".join(durumlar))
            else:
                status_lines.append(f"🤖 **Ana Bot ({main_bot.mention}):** `Çevrimiçi (Aktif)`")
        else:
            status_lines.append(f"🤖 **Ana Bot Durumu:** Sunucu üzerinden sorgulanamadı")

    # 2. Eğer ERLC_API_KEY tanımlıysa doğrudan API sorgula
    if ERLC_API_KEY:
        try:
            headers = {"Server-Key": ERLC_API_KEY}
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.erlc.gg/v2/server?Queue=true", headers=headers, timeout=4) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        cur = data.get("CurrentPlayers", 0)
                        max_p = data.get("MaxPlayers", 40)
                        q = data.get("Queue", [])
                        q_count = len(q) if isinstance(q, list) else int(q or 0)
                        s_name = data.get("Name", "Piyade Roleplay")
                        status_lines.append(
                            f"🌐 **ER:LC API Canlı Verisi:**\n"
                            f"• Sunucu: **{s_name}**\n"
                            f"• Aktif Oyuncu: **{cur} / {max_p}**\n"
                            f"• Sırada Bekleyen: **{q_count} Kişi**"
                        )
        except Exception:
            pass

    # 3. RP Duyuru kanalındaki son mesajdan rol aktifliğini oku
    if guild:
        rp_kanal = guild.get_channel(RP_DUYURU_KANAL_ID)
        if rp_kanal:
            try:
                son_mesajlar = [m async for m in rp_kanal.history(limit=1)]
                if son_mesajlar:
                    son_m = son_mesajlar[0]
                    tarih = son_m.created_at.strftime("%d.%m.%Y %H:%M")
                    temiz_metin = son_m.clean_content.replace('\n', ' ')[:140]
                    status_lines.append(f"📢 **Son RP Duyurusu ({tarih}):**\n> *{temiz_metin}...*")
            except Exception:
                pass

    return "\n\n".join(status_lines) if status_lines else "• Bilgi alınamadı."


# =====================================================================
# EMBED OLUŞTURUCULAR
# =====================================================================

def build_category_embed(kategori: str, extra_info: str = "") -> discord.Embed:
    """
    Seçilen kategoriye ait büyük resimli ve ince uzun çizgili embed'i üretir.
    """
    embed_map = {
        "anasayfa": (
            f"ℹ️ {SUNUCU_ADI} • Resmi Sunucu Rehberi",
            ANASAYFA_METIN,
            RENK_ANA
        ),
        "genel_rehber": (
            "ℹ️ Genel Sunucu Rehberi & Kanal Düzeni",
            KANALLAR_METIN,
            RENK_ANA
        ),
        "tum_kurallar": (
            "ℹ️ Tüm Kurallar & Ceza Puan Sistemi",
            TUM_KURALLAR_METIN,
            RENK_KIRMIZI
        ),
        "rp_terimleri": (
            "ℹ️ Roleplay Terimleri Sözlüğü (RM1 - RM17)",
            RP_TERIMLERI_METIN,
            RENK_ALTIN
        ),
        "kayit_sistemi": (
            "ℹ️ Kayıt Sistemi & Whitelist Kılavuzu",
            KAYIT_SISTEMI_METIN,
            RENK_YESIL
        ),
        "cete_sistemi": (
            "ℹ️ İllegal Dünyası, Çete Sistemi & Meth Üretimi",
            CETE_SISTEMI_METIN,
            RENK_MOR
        ),
        "vs_sistemi": (
            "ℹ️ Vs Talep Sistemi & Kademe (Rank Up)",
            VS_TALEP_METIN,
            RENK_ANA
        ),
        "erlc_bilgi": (
            "ℹ️ ER:LC Oyun Bilgisi & Canlı Sunucu Durumu",
            ERLC_BILGI_METIN + (f"\n\n{DIVIDER}\n\n### 📡 ANLIK CANLI SUNUCU VERİLERİ\n{extra_info}" if extra_info else ""),
            RENK_ANA
        ),
        "diger": (
            "ℹ️ Diğer Bilgiler & Destek Merkezi",
            DIGER_METIN,
            RENK_TURUNCU
        )
    }

    title, desc, color = embed_map.get(kategori, embed_map["anasayfa"])

    embed = discord.Embed(
        title=title,
        description=desc,
        color=color
    )
    # Büyük resim iliştirme
    embed.set_image(url="attachment://rehber_banner.jpg")
    embed.set_footer(text=FOOTER_TEXT)
    return embed


def get_kanal_paneli_embed() -> discord.Embed:
    """
    Sunucu kanalında (#rehber) sabit duracak ana tanıtım paneli embed'i.
    """
    desc = (
        f"# 📖 {SUNUCU_ADI} • RESMİ REHBER MERKEZİ\n\n"
        f"{DIVIDER}\n\n"
        "Değerli üyemiz, sunucumuzun tüm sistemlerini, kurallarını, kayıt aşamalarını ve "
        "oyun dinamiklerini tek bir noktadan öğrenmeniz için hazırladığımız rehber sistemine hoş geldiniz!\n\n"
        f"{DIVIDER}\n\n"
        "✨ **Kişiye Özel İnteraktif DM Rehberi:**\n"
        "Sunucu kanalındaki sohbet akışını ve görüntü düzenini korumak amacıyla; "
        "aşağıdaki **`Rehberi Başlat`** butonuna tıkladığınızda rehber paneli **Direkt Mesaj (DM)** "
        "kutunuza özel olarak iletilecektir.\n\n"
        f"{DIVIDER}\n\n"
        "📌 **Rehberde Bulunan Başlıca Kategoriler:**\n"
        "• ℹ️ **Anasayfa & Sunucu Düzeni** *(Tüm Kanalları Göster Ayarı)*\n"
        "• ℹ️ **Genel Sunucu Rehberi** *(Tüm 23 Kanalın Detayları)*\n"
        "• ℹ️ **Tüm Kurallar** *(M1-M13, D1-D3, Y1-Y5 & Ceza Puanları)*\n"
        "• ℹ️ **RP Terimleri** *(RM1-RM17 Örnekli Açıklamalar)*\n"
        "• ℹ️ **Kayıt Sistemi** *(Aşama Aşama Whitelist Kılavuzu)*\n"
        "• ℹ️ **Çete Sistemi** *(Parseller, Savaşlar, 7 Gün Cooldown & Meth)*\n"
        "• ℹ️ **Vs Talep Sistemi** *(PvP & Drive Kapışmaları, Kademe 1-7)*\n"
        "• ℹ️ **ER:LC Bilgi** *(Canlı Oyuncu Sayısı & Safezonelar)*\n"
        "• ℹ️ **Diğer...** *(Ticket & Destek Yönlendirmesi)*\n\n"
        f"{DIVIDER}\n\n"
        "👉 **Hemen başlamak için aşağıdaki butona tıklayınız!**"
    )

    embed = discord.Embed(
        description=desc,
        color=RENK_ANA
    )
    embed.set_image(url="attachment://rehber_banner.jpg")
    embed.set_footer(text=FOOTER_TEXT)
    return embed


# =====================================================================
# DM İÇERİSİNDEKİ SEÇİM MENÜSÜ & VIEW
# =====================================================================

class RehberDMSelectMenu(Select):
    def __init__(self, bot: discord.Client, aktif_kategori: str = "anasayfa"):
        self.bot = bot
        options = [
            discord.SelectOption(
                label="Anasayfa",
                description="Sunucu tanıtımı ve 'Tüm Kanalları Göster' ayarı",
                emoji="ℹ️",
                value="anasayfa",
                default=(aktif_kategori == "anasayfa")
            ),
            discord.SelectOption(
                label="Genel Sunucu Rehberi",
                description="Tüm kanalların detaylı açıklamaları ve düzeni",
                emoji="ℹ️",
                value="genel_rehber",
                default=(aktif_kategori == "genel_rehber")
            ),
            discord.SelectOption(
                label="Tüm Kurallar",
                description="M1-M13, D1-D3, Y1-Y5 ve ceza puan kademeleri",
                emoji="ℹ️",
                value="tum_kurallar",
                default=(aktif_kategori == "tum_kurallar")
            ),
            discord.SelectOption(
                label="RP Terimleri",
                description="RM1-RM17 terimleri ve hatalı rol örnekleri",
                emoji="ℹ️",
                value="rp_terimleri",
                default=(aktif_kategori == "rp_terimleri")
            ),
            discord.SelectOption(
                label="Kayıt Sistemi",
                description="Aşama aşama Whitelist ve Roblox başvuru kılavuzu",
                emoji="ℹ️",
                value="kayit_sistemi",
                default=(aktif_kategori == "kayit_sistemi")
            ),
            discord.SelectOption(
                label="Çete Sistemi",
                description="Parseller, savaşlar, 7 gün cooldown ve meth üretimi",
                emoji="ℹ️",
                value="cete_sistemi",
                default=(aktif_kategori == "cete_sistemi")
            ),
            discord.SelectOption(
                label="Vs Talep Sistemi",
                description="1v1 PvP & Drive düelloları ve Kademe 1-7",
                emoji="ℹ️",
                value="vs_sistemi",
                default=(aktif_kategori == "vs_sistemi")
            ),
            discord.SelectOption(
                label="ER:LC Bilgi",
                description="Canlı oyuncu sayısı, RP durumu ve Safezonelar",
                emoji="ℹ️",
                value="erlc_bilgi",
                default=(aktif_kategori == "erlc_bilgi")
            ),
            discord.SelectOption(
                label="Diğer...",
                description="Ticket açma ve canlı destek yönlendirmesi",
                emoji="ℹ️",
                value="diger",
                default=(aktif_kategori == "diger")
            ),
        ]
        super().__init__(
            placeholder="🔍 İncelemek istediğiniz kategoriyi seçiniz...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="select_rehber_dm_kategori"
        )

    async def callback(self, interaction: discord.Interaction):
        kategori = self.values[0]
        await interaction.response.defer()

        extra_info = ""
        if kategori == "erlc_bilgi":
            extra_info = await get_live_erlc_info(self.bot)

        embed = build_category_embed(kategori, extra_info=extra_info)
        new_view = RehberDMView(self.bot, aktif_kategori=kategori)
        await interaction.edit_original_response(embed=embed, view=new_view)


class RehberDMView(View):
    """
    Kullanıcının DM kutusuna gönderilen interaktif rehber view'ı.
    Açılır menü ve hızlı butonlar içerir.
    """
    def __init__(self, bot: discord.Client, aktif_kategori: str = "anasayfa"):
        super().__init__(timeout=None)
        self.bot = bot
        self.aktif_kategori = aktif_kategori

        # 1. Kategori Seçim Menüsü
        self.add_item(RehberDMSelectMenu(bot, aktif_kategori=aktif_kategori))

        # 2. Hızlı Erişim Butonları (Row 1)
        btn_anasayfa = Button(label="Anasayfa", emoji="🏠", style=discord.ButtonStyle.secondary, custom_id="dm_btn_anasayfa", row=1)
        btn_anasayfa.callback = self.on_anasayfa
        self.add_item(btn_anasayfa)

        btn_kayit = Button(label="Kayıt Rehberi", emoji="📋", style=discord.ButtonStyle.success, custom_id="dm_btn_kayit", row=1)
        btn_kayit.callback = self.on_kayit
        self.add_item(btn_kayit)

        btn_kurallar = Button(label="Tüm Kurallar", emoji="⚖️", style=discord.ButtonStyle.primary, custom_id="dm_btn_kurallar", row=1)
        btn_kurallar.callback = self.on_kurallar
        self.add_item(btn_kurallar)

        # 3. Canlı Bilgi ve Destek Butonları (Row 2)
        btn_erlc = Button(label="ER:LC Canlı Bilgi", emoji="🎮", style=discord.ButtonStyle.primary, custom_id="dm_btn_erlc", row=2)
        btn_erlc.callback = self.on_erlc
        self.add_item(btn_erlc)

        btn_destek = Button(label="Destek Talebi Aç", emoji="🎫", style=discord.ButtonStyle.link, url=TICKET_KANAL_LINK, row=2)
        self.add_item(btn_destek)

    async def _update_view(self, interaction: discord.Interaction, kategori: str):
        await interaction.response.defer()
        extra_info = ""
        if kategori == "erlc_bilgi":
            extra_info = await get_live_erlc_info(self.bot)
        embed = build_category_embed(kategori, extra_info=extra_info)
        new_view = RehberDMView(self.bot, aktif_kategori=kategori)
        await interaction.edit_original_response(embed=embed, view=new_view)

    async def on_anasayfa(self, interaction: discord.Interaction):
        await self._update_view(interaction, "anasayfa")

    async def on_kayit(self, interaction: discord.Interaction):
        await self._update_view(interaction, "kayit_sistemi")

    async def on_kurallar(self, interaction: discord.Interaction):
        await self._update_view(interaction, "tum_kurallar")

    async def on_erlc(self, interaction: discord.Interaction):
        await self._update_view(interaction, "erlc_bilgi")


# =====================================================================
# SUNUCU KANALINDAKİ SABİT PANEL VIEW'I
# =====================================================================

class KanalRehberPanelView(View):
    """
    Sunucu kanalındaki (#1556687054526611486) sabit panelin kalıcı butonu.
    Kullanıcı butona bastığında DM üzerinden rehber panelini gönderir.
    """
    def __init__(self, bot: discord.Client = None):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(
        label="📖 Rehberi Başlat (DM Kutunuza Gönderir)",
        emoji="📬",
        style=discord.ButtonStyle.success,
        custom_id="btn_rehber_dm_ac"
    )
    async def btn_dm_gonder(self, interaction: discord.Interaction, button: Button):
        user = interaction.user
        bot = self.bot or interaction.client

        # Kullanıcıya DM göndermeyi dene
        try:
            embed = build_category_embed("anasayfa")
            view = RehberDMView(bot, aktif_kategori="anasayfa")

            if os.path.exists(BANNER_PATH):
                file = discord.File(BANNER_PATH, filename="rehber_banner.jpg")
                await user.send(file=file, embed=embed, view=view)
            else:
                await user.send(embed=embed, view=view)

            await interaction.response.send_message(
                f"📬 **Rehber Paneliniz DM Kutunuza İletildi, {user.mention}!**\n\n"
                "> Lütfen özel mesajlarınızı kontrol ediniz. Açılır menü ve butonları kullanarak sunucumuz hakkındaki tüm bilgilere oradan erişebilirsiniz.\n\n"
                "*⚠️ Eğer mesaj ulaşmadıysa Discord gizlilik ayarlarınızdan direkt mesajların sunucu üyelerine açık olduğundan emin olunuz.*",
                ephemeral=True
            )
        except discord.Forbidden:
            await interaction.response.send_message(
                f"❌ **DM Kutunuz Kapalı, {user.mention}!**\n\n"
                "> Rehber panelini size özel mesaj olarak iletebilmemiz için lütfen:\n"
                "> 1️⃣ Sol üstteki sunucu adına tıklayıp **Gizlilik Ayarları** kısmına giriniz.\n"
                "> 2️⃣ **Direkt Mesajlar** seçeneğini aktif hale getiriniz.\n"
                "> 3️⃣ Ardından butona tekrar basınız.",
                ephemeral=True
            )
        except Exception as e:
            await interaction.response.send_message(
                f"❌ Bir hata oluştu: `{e}`. Lütfen yetkililere bildiriniz.",
                ephemeral=True
            )


async def setup(bot: discord.Client):
    """View modülü setup kancası."""
    pass
