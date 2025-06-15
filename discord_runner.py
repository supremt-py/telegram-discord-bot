import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

telegram_to_discord = {}

async def send_to_discord(text, telegram_msg_id=None, media_path=None, original_filename=None):
    channel_id = int(os.getenv("DISCORD_CHANNEL_ID"))
    channel = bot.get_channel(channel_id)
    if not channel:
        print("Hedef Discord kanalı bulunamadı.")
        return

    try:
        if media_path:
            # Gerçek dosya adını kullan, yoksa varsayılan ver
            filename = original_filename or os.path.basename(media_path)
            with open(media_path, "rb") as f:
                discord_file = discord.File(f, filename=filename)
                msg = await channel.send(content=text, file=discord_file)
        else:
            msg = await channel.send(content=text)

        if telegram_msg_id:
            telegram_to_discord[telegram_msg_id] = msg.id
    except Exception as e:
        print(f"Discord'a mesaj gönderilirken hata oluştu: {e}")

async def start_discord_bot():
    await bot.start(os.getenv("DISCORD_TOKEN"))
