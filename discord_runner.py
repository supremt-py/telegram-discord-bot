import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

telegram_to_discord = {}

@bot.event
async def on_ready():
    print(f"Discord bot aktif: {bot.user}")

async def send_to_discord(text, telegram_msg_id=None):
    channel_id = os.getenv("DISCORD_CHANNEL_ID")
    if not channel_id:
        print("HATA: DISCORD_CHANNEL_ID tanımlı değil!")
        return

    channel = bot.get_channel(int(channel_id))
    if not channel:
        print("Hedef Discord kanalı bulunamadı.")
        return

    try:
        # Mesajı bir task olarak başlat
        await channel.send(text)
    except Exception as e:
        print(f"Discord'a mesaj gönderilirken hata oluştu: {e}")

async def start_discord_bot():
    await bot.start(os.getenv("DISCORD_TOKEN"))
