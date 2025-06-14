import os
import discord
import asyncio
from discord.ext import commands
from langdetect import detect
from deep_translator import GoogleTranslator

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
telegram_to_discord = {}

async def send_to_discord(message, telegram_msg_id=None):
    await bot.wait_until_ready()
    channel = bot.get_channel(DISCORD_CHANNEL_ID)

    try:
        # Türkçe ise İngilizceye çevir
        lang = detect(message)
        if lang == "tr":
            translated = GoogleTranslator(source="tr", target="en").translate(message)
            text_to_send = f"{message}\n\n**Translation:** {translated}"
        else:
            text_to_send = message

        discord_message = await channel.send(text_to_send)

        if telegram_msg_id:
            telegram_to_discord[telegram_msg_id] = discord_message.id

    except Exception as e:
        print(f"Discord'a gönderme hatası: {e}")

def run_discord_bot():
    loop = asyncio.get_event_loop()
    loop.create_task(bot.start(DISCORD_TOKEN))
