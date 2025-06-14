import os
import discord
import asyncio
from discord.ext import commands
from googletrans import Translator
from langdetect import detect

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
translator = Translator()
telegram_to_discord = {}

async def send_to_discord(message, telegram_msg_id=None):
    await bot.wait_until_ready()
    channel = bot.get_channel(DISCORD_CHANNEL_ID)

    try:
        # Türkçe olup olmadığını kontrol et
        lang = detect(message)
        if lang == 'tr':
            translated = translator.translate(message, src='tr', dest='en').text
            text_to_send = f"{message}\n\n**Translation:** {translated}"
        else:
            text_to_send = message

        discord_message = await channel.send(text_to_send)

        # Telegram mesajı ID'si ile eşleştir
        if telegram_msg_id:
            telegram_to_discord[telegram_msg_id] = discord_message.id

    except Exception as e:
        print(f"Discord'a gönderme hatası: {e}")

def run_discord_bot():
    loop = asyncio.get_event_loop()
    loop.create_task(bot.start(DISCORD_TOKEN))
