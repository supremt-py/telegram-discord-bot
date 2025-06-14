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

async def send_to_discord(content, file_path=None):
    channel_id = int(os.getenv("DISCORD_CHANNEL_ID"))
    channel = bot.get_channel(channel_id)
    if not channel:
        print("Hedef Discord kanalı bulunamadı.")
        return

    try:
        if file_path:
            with open(file_path, "rb") as f:
                discord_file = discord.File(f)
                await channel.send(content, file=discord_file)
        else:
            await channel.send(content)
    except Exception as e:
        print(f"Discord'a mesaj gönderilirken hata oluştu: {e}")

async def start_discord_bot():
    await bot.start(os.getenv("DISCORD_TOKEN"))
