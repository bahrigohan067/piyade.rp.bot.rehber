# -*- coding: utf-8 -*-
import time
import discord
from discord.ext import commands

from config import (
    SUNUCU_ADI, ERLC_SUNUCU_KODU, ROBLOX_GRUP_LINK,
    KAYIT_KANAL_ID, ROBLOX_GRUP_KANAL_ID, TICKET_KANAL_ID,
    REHBER_PANEL_KANAL_ID, RENK_ANA, RENK_YESIL
)

class RehberListener(commands.Cog):
    """
    Sohbette sıkça sorulan soruları tespit eden ve kullanıcılara
    spam yapmadan (cooldown korumalı) yardımcı olan akıllı dinleyici.
    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.kullanici_cooldown = {}   # {user_id: timestamp}
        self.kanal_cooldown = {}       # {channel_id: timestamp}

    def cooldown_var_mi(self, user_id: int, channel_id: int) -> bool:
        simdi = time.time()
        # Kullanıcı bazlı 60 saniye cooldown
        if user_id in self.kullanici_cooldown and (simdi - self.kullanici_cooldown[user_id]) < 60:
            return True
        # Kanal bazlı 30 saniye cooldown
        if channel_id in self.kanal_cooldown and (simdi - self.kanal_cooldown[channel_id]) < 30:
            return True
        return False

    def cooldown_guncelle(self, user_id: int, channel_id: int):
        simdi = time.time()
        self.kullanici_cooldown[user_id] = simdi
        self.kanal_cooldown[channel_id] = simdi

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # Botların mesajlarını ve DM'leri yoksay
        if message.author.bot or not message.guild:
            return

        icerik = message.content.lower().strip()

        # -------------------------------------------------------------
        # 1. Kayıt / Whitelist Soruları
        # -------------------------------------------------------------
        kayit_kaliplari = [
            "nasıl kayıt", "kayıt nasıl", "kayıt olamıyorum", "kayıt nerden",
            "whitelist nasıl", "wl nasıl", "kayıt olmak istiyorum"
        ]
        if any(kalip in icerik for kalip in kayit_kaliplari):
            if self.cooldown_var_mi(message.author.id, message.channel.id):
                return
            self.cooldown_guncelle(message.author.id, message.channel.id)

            embed = discord.Embed(
                title="📋 Kayıt ve Whitelist Yardımı",
                description=(
                    f"Merhaba {message.author.mention}! Sunucumuzda rol yapabilmek için:\n\n"
                    f"1️⃣ <#{KAYIT_KANAL_ID}> kanalındaki **Kayıt Ol** butonuna basınız.\n"
                    f"2️⃣ Size özel açılan gizli konudan başvurunuzu tamamlayınız.\n"
                    f"3️⃣ Roblox grubumuz ([Piyade RP | Los Angeles]({ROBLOX_GRUP_LINK})) üzerinden onay alınız.\n\n"
                    f"💡 *Tüm detaylı aşamalar için <#{REHBER_PANEL_KANAL_ID}> kanalındaki rehber butonuna tıklayabilirsiniz.*"
                ),
                color=RENK_YESIL
            )
            try:
                await message.reply(embed=embed, mention_author=False)
            except Exception:
                pass
            return

        # -------------------------------------------------------------
        # 2. ER:LC Giriş Kodu / Sunucu Kodu Soruları
        # -------------------------------------------------------------
        kod_kaliplari = [
            "sunucu kodu", "erlc kodu", "oyun kodu", "server code",
            "kod ne", "kod nedir", "kodu ne", "sunucuya nasıl girerim", "oyuna nasıl girerim"
        ]
        if any(kalip in icerik for kalip in kod_kaliplari):
            if self.cooldown_var_mi(message.author.id, message.channel.id):
                return
            self.cooldown_guncelle(message.author.id, message.channel.id)

            embed = discord.Embed(
                title="🎮 ER:LC Sunucu Katılım Kodu",
                description=(
                    f"Merhaba {message.author.mention}!\n\n"
                    f"📌 **Sunucu Katılım Kodu:** **`{ERLC_SUNUCU_KODU}`**\n\n"
                    "Roblox ER:LC içerisinde **Servers ➡️ Join by Code** kısmına yukarıdaki kodu yazarak doğrudan bağlanabilirsiniz!\n"
                    f"💡 *Safezone ve kurallar için <#{REHBER_PANEL_KANAL_ID}> kanalını ziyaret edebilirsiniz.*"
                ),
                color=RENK_ANA
            )
            try:
                await message.reply(embed=embed, mention_author=False)
            except Exception:
                pass
            return

        # -------------------------------------------------------------
        # 3. Roblox Grubu Soruları
        # -------------------------------------------------------------
        grup_kaliplari = ["roblox grubu", "grup linki", "grup link", "roblox link"]
        if any(kalip in icerik for kalip in grup_kaliplari):
            if self.cooldown_var_mi(message.author.id, message.channel.id):
                return
            self.cooldown_guncelle(message.author.id, message.channel.id)

            embed = discord.Embed(
                title="🔗 Roblox Grubu",
                description=(
                    f"Merhaba {message.author.mention}!\n\n"
                    f"👉 **Roblox Grubumuz:** [Piyade RP | Los Angeles]({ROBLOX_GRUP_LINK})\n"
                    f"Grup onayınızı tamamlamak için <#{ROBLOX_GRUP_KANAL_ID}> kanalını ziyaret edebilirsiniz."
                ),
                color=RENK_ANA
            )
            try:
                await message.reply(embed=embed, mention_author=False)
            except Exception:
                pass
            return

        # -------------------------------------------------------------
        # 4. Destek / Ticket Soruları
        # -------------------------------------------------------------
        destek_kaliplari = ["destek talebi", "ticket nasıl", "bilet nasıl", "şikayet etmek"]
        if any(kalip in icerik for kalip in destek_kaliplari):
            if self.cooldown_var_mi(message.author.id, message.channel.id):
                return
            self.cooldown_guncelle(message.author.id, message.channel.id)

            embed = discord.Embed(
                title="🚨 Destek & Şikayet",
                description=(
                    f"Merhaba {message.author.mention}!\n\n"
                    f"Bir sorun veya kural ihlali bildirmek için <#{TICKET_KANAL_ID}> kanalından destek talebi açabilirsiniz."
                ),
                color=RENK_ANA
            )
            try:
                await message.reply(embed=embed, mention_author=False)
            except Exception:
                pass
            return


async def setup(bot: commands.Bot):
    await bot.add_cog(RehberListener(bot))
