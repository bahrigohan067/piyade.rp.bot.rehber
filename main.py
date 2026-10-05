# -*- coding: utf-8 -*-
import sys
import os

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import discord
from discord.ext import commands
from discord import app_commands
from config import TOKEN, GUILD_ID, SUNUCU_ADI, REHBER_PANEL_KANAL_ID

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
try:
    intents.members = True
    intents.presences = True
except Exception:
    pass

class RehberBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # 1. Cogs Klasörünü Otomatik Yükleme
        cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
        for filename in sorted(os.listdir(cogs_dir)):
            if filename.endswith(".py") and not filename.startswith("__"):
                try:
                    await self.load_extension(f"cogs.{filename[:-3]}")
                    print(f"✅ Yüklendi: {filename}")
                except Exception as e:
                    print(f"❌ Hata: {filename} → {e}")

        # 2. Kalıcı (Persistent) Sunucu Kanal Paneli View Kaydı
        from cogs.rehber_views import KanalRehberPanelView
        self.add_view(KanalRehberPanelView(self))
        print("🔗 Kalıcı Sunucu Rehber Paneli Görünümü (KanalRehberPanelView) kaydedildi.")

        # 3. Akıllı Otomatik Slash Komut Senkronizasyonu
        try:
            guild = discord.Object(id=GUILD_ID)
            self.tree.copy_global_to(guild=guild)

            yerel_komutlar = self.tree.get_commands(guild=guild)
            kayitli_komutlar = await self.tree.fetch_commands(guild=guild)

            if len(yerel_komutlar) != len(kayitli_komutlar):
                synced = await self.tree.sync(guild=guild)
                print(f"[SYNC] Komut sayısı değişti ({len(kayitli_komutlar)} → {len(synced)}). Senkronize edildi.")
            else:
                print(f"[SYNC] Komutlar güncel ({len(kayitli_komutlar)} komut). Sync atlandı.")
        except Exception as e:
            print(f"[SYNC] Senkronizasyon hatası: {e}")

bot = RehberBot()

@bot.event
async def on_ready():
    print("=" * 60)
    print(f"🚀 {SUNUCU_ADI} — Rehber Botu Başarıyla Giriş Yaptı!")
    print(f"🤖 Bot Adı: {bot.user}")
    print(f"🆔 Bot ID: {bot.user.id}")
    print(f"🏰 Hedef Sunucu (Guild ID): {GUILD_ID}")
    print(f"📍 Rehber Paneli Kanalı: {REHBER_PANEL_KANAL_ID}")
    print(f"🔑 Token Ortam Değişkeni: TOKEN_REHBER (Aktif)")
    print("=" * 60)

    # Bot Durumu (Rich Presence)
    aktivite = discord.Activity(
        type=discord.ActivityType.watching,
        name="📖 /rehber | DM Rehberi"
    )
    await bot.change_presence(status=discord.Status.online, activity=aktivite)

@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    import traceback
    traceback.print_exception(type(error), error, error.__traceback__)

    if isinstance(error, app_commands.CommandOnCooldown):
        kalan = int(error.retry_after)
        msg = f"⏳ Bu komutu tekrar kullanabilmek için **{kalan} saniye** beklemelisiniz."
    elif isinstance(error, app_commands.MissingPermissions):
        msg = "❌ Bu komutu kullanmak için gerekli yetkilere sahip değilsiniz."
    else:
        msg = "❌ Komut çalışırken bir hata oluştu."

    try:
        if interaction.response.is_done():
            await interaction.followup.send(msg, ephemeral=True)
        else:
            await interaction.response.send_message(msg, ephemeral=True)
    except Exception:
        pass

if __name__ == "__main__":
    if not TOKEN:
        print("❌ HATA: Discord Bot TOKEN_REHBER tanımlı değil!")
        print("Lütfen Railway panelinden veya .env dosyasından TOKEN_REHBER değişkenini tanımlayın.")
        sys.exit(1)

    bot.run(TOKEN)
