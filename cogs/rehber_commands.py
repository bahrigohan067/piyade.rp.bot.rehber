# -*- coding: utf-8 -*-
import os
import discord
from discord.ext import commands
from discord import app_commands

from config import (
    SUNUCU_ADI, GUILD_ID, REHBER_PANEL_KANAL_ID,
    YONETIM_ROLLER, BANNER_PATH
)
from cogs.rehber_views import (
    KanalRehberPanelView,
    RehberDMView,
    get_kanal_paneli_embed,
    build_category_embed
)

def yetkili_mi(member: discord.Member) -> bool:
    """Kullanıcının yönetici veya izinli yetkili olup olmadığını denetler."""
    if member.guild_permissions.administrator:
        return True
    return any(r.id in YONETIM_ROLLER for r in member.roles)


class RehberCommands(commands.Cog):
    """
    Piyade RP — Birleşik Rehber Paneli Kurulum ve Tetikleme Komutları
    (Tüm ayrı slash komutları kaldırılmış ve tek bir interaktif DM paneline birleştirilmiştir.)
    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # -----------------------------------------------------------------
    # /rehber-paneli-kur — Kanala Sabit Kalıcı Paneli Kurar
    # -----------------------------------------------------------------
    @app_commands.command(
        name="rehber-paneli-kur",
        description="Belirtilen kanala sabit ve kalıcı Ana Rehber Panelini kurar."
    )
    @app_commands.describe(
        kanal=f"Rehber panelinin kurulacağı metin kanalı (Varsayılan: #1556687054526611486)"
    )
    async def cmd_rehber_paneli_kur(self, interaction: discord.Interaction, kanal: discord.TextChannel = None):
        if not yetkili_mi(interaction.user):
            await interaction.response.send_message(
                "❌ Bu komutu yalnızca **Sunucu Yönetimi** kullanabilir.",
                ephemeral=True
            )
            return

        await interaction.response.defer(ephemeral=True)

        guild = interaction.guild or self.bot.get_guild(GUILD_ID)
        hedef_kanal = kanal or guild.get_channel(REHBER_PANEL_KANAL_ID) or interaction.channel

        embed = get_kanal_paneli_embed()
        view = KanalRehberPanelView(self.bot)

        try:
            if os.path.exists(BANNER_PATH):
                file = discord.File(BANNER_PATH, filename="rehber_banner.jpg")
                await hedef_kanal.send(file=file, embed=embed, view=view)
            else:
                await hedef_kanal.send(embed=embed, view=view)

            await interaction.followup.send(
                f"✅ **Ana Rehber Paneli** başarıyla {hedef_kanal.mention} kanalına kuruldu!\n"
                "> Kullanıcılar butona tıkladığında tüm rehber kategorileri DM üzerinden özel olarak iletilecektir.",
                ephemeral=True
            )
        except Exception as e:
            await interaction.followup.send(
                f"❌ Panel kurulurken bir hata oluştu: `{e}`",
                ephemeral=True
            )

    # -----------------------------------------------------------------
    # /rehber — Rehberi Doğrudan DM Olarak Çağırma Komutu
    # -----------------------------------------------------------------
    @app_commands.command(
        name="rehber",
        description="Piyade RP interaktif rehber panelini DM kutunuza gönderir."
    )
    async def cmd_rehber(self, interaction: discord.Interaction):
        user = interaction.user
        try:
            embed = build_category_embed("anasayfa")
            view = RehberDMView(self.bot, aktif_kategori="anasayfa")

            if os.path.exists(BANNER_PATH):
                file = discord.File(BANNER_PATH, filename="rehber_banner.jpg")
                await user.send(file=file, embed=embed, view=view)
            else:
                await user.send(embed=embed, view=view)

            await interaction.response.send_message(
                f"📬 **Rehber Paneliniz DM Kutunuza Gönderildi, {user.mention}!**\n"
                "> Lütfen özel mesajlarınızı kontrol ediniz.",
                ephemeral=True
            )
        except discord.Forbidden:
            await interaction.response.send_message(
                f"❌ **DM Kutunuz Kapalı, {user.mention}!**\n"
                "> Rehber panelini size iletebilmemiz için lütfen **Sunucu Ayarları ➡️ Gizlilik ➡️ Direkt Mesajlar** seçeneğini aktif ediniz.",
                ephemeral=True
            )
        except Exception as e:
            await interaction.response.send_message(
                f"❌ Bir hata oluştu: `{e}`",
                ephemeral=True
            )


async def setup(bot: commands.Bot):
    await bot.add_cog(RehberCommands(bot))
