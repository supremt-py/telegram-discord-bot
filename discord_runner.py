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
    await bot.wait_until_ready()

    channel_id = os.getenv("DISCORD_CHANNEL_ID")
    if not channel_id:
        print("Hata: DISCORD_CHANNEL_ID ortam değişkeni tanımlı değil.")
        return

    try:
        channel_id = int(channel_id)
        channel = bot.get_channel(channel_id)
        if not channel:
            print("Hedef Discord kanalı bulunamadı.")
            return

        msg = await channel.send(text)
        if telegram_msg_id:
            telegram_to_discord[telegram_msg_id] = msg.id
    except Exception as e:
        print(f"Discord'a mesaj gönderilirken hata oluştu: {e}")
