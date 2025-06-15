import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

telegram_to_discord = {}

@bot.event
async def on_ready():
    print(f"Discord bot aktif: {bot.user}")

async def send_to_discord(text, telegram_msg_id=None, media_path=None):
    channel_id = int(os.getenv("DISCORD_CHANNEL_ID"))
    channel = bot.get_channel(channel_id)
    if not channel:
        print("Hedef Discord kanalı bulunamadı.")
        return

    try:
        if media_path:
            # 🔧 Uzantısı doğru olan bir dosya adı üretelim
            ext = ".jpg" if media_path.endswith(".jpg") else ".png"  # varsayalım görsel
            filename = os.path.basename(media_path)
            if not filename.endswith(ext):
                filename += ext

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
