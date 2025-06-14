import os
import discord
from discord.ext import commands

# Discord bot için gerekli izinleri ayarla
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Telegram mesaj ID'si ile Discord mesaj ID'si eşleştirmesi
telegram_to_discord = {}

@bot.event
async def on_ready():
    print(f"Discord bot aktif: {bot.user}")

async def send_to_discord(text, telegram_msg_id=None):
    await bot.wait_until_ready()
    channel_id = int(os.getenv("DISCORD_CHANNEL_ID"))
    channel = bot.get_channel(channel_id)
    if not channel:
        print("Hedef Discord kanalı bulunamadı.")
        return
    msg = await channel.send(text)
    if telegram_msg_id:
        telegram_to_discord[telegram_msg_id] = msg.id
