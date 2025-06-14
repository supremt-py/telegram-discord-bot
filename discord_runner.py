import os
import discord
from discord.ext import commands

# Gerekli izinler
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Telegram mesaj ID ↔ Discord mesaj ID eşleşmesi
telegram_to_discord = {}

@bot.event
async def on_ready():
    print(f"Discord bot aktif: {bot.user}")

async def send_to_discord(text, telegram_msg_id=None):
    await bot.wait_until_ready()
    try:
        channel_id = os.getenv("DISCORD_CHANNEL_ID")
        if not channel_id:
            print("HATA: DISCORD_CHANNEL_ID tanımlı değil!")
            return

        channel = bot.get_channel(int(channel_id))
        if not channel:
            print("HATA: Kanal bulunamadı! Kanal ID yanlış ya da botun erişimi yok.")
            return

        msg = await channel.send(text)
        if telegram_msg_id:
            telegram_to_discord[telegram_msg_id] = msg.id
    except Exception as e:
        print(f"Discord mesaj gönderme hatası: {e}")
