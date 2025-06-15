import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

telegram_to_discord = {}

@bot.event
async def on_ready():
    print(f"Discord bot aktif: {bot.user}")

async def send_to_discord(text, telegram_msg_id=None):
    channel_id = int(os.getenv("DISCORD_CHANNEL_ID"))
    channel = bot.get_channel(channel_id)
    if not channel:
        print("Hedef Discord kanalı bulunamadı.")
        return

    try:
        msg = await channel.send(text)
        if telegram_msg_id:
            telegram_to_discord[telegram_msg_id] = msg.id
    except Exception as e:
        print(f"Discord'a mesaj gönderilirken hata oluştu: {e}")

async def start_discord_bot():
    await bot.start(os.getenv("DISCORD_TOKEN"))
