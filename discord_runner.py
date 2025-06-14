import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

telegram_to_discord = {}

@bot.event
async def on_ready():
    print(f"Discord bot aktif: {bot.user}")

async def send_to_discord(text, file=None):
    await bot.wait_until_ready()
    channel_id = int(os.getenv("DISCORD_CHANNEL_ID"))
    channel = bot.get_channel(channel_id)

    if not channel:
        print("Hedef Discord kanalı bulunamadı.")
        return

    try:
        if file:
            await channel.send(content=text, file=file)
        else:
            await channel.send(content=text)
    except Exception as e:
        print(f"Discord'a mesaj gönderilirken hata oluştu: {e}")

async def start_discord_bot():
    await bot.start(os.getenv("DISCORD_TOKEN"))
