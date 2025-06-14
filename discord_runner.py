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
    try:
        channel_id_str = os.getenv("DISCORD_CHANNEL_ID")
        print(f"[DEBUG] Ortamdan gelen kanal ID: {channel_id_str}")
        if not channel_id_str:
            print("[HATA] DISCORD_CHANNEL_ID ortam değişkeni tanımlı değil.")
            return

        channel_id = int(channel_id_str)
        channel = bot.get_channel(channel_id)
        if not channel:
            print(f"[HATA] Kanal bulunamadı! ID: {channel_id}")
            return

        msg = await channel.send(text)
        print(f"[OK] Discord'a mesaj gönderildi. Mesaj ID: {msg.id}")

        if telegram_msg_id:
            telegram_to_discord[telegram_msg_id] = msg.id

    except Exception as e:
        print(f"[EXCEPTION] Discord'a mesaj gönderilirken hata oluştu: {e}")
