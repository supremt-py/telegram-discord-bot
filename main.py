import os
import sys
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

from telegram.ext import Updater, MessageHandler, Filters
import threading
from discord_bot import run_discord_bot, send_to_discord
import asyncio

# Ortam değişkenlerinden token'ları al
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def forward_channel_post(update, context):
    if update.channel_post:
        text = update.channel_post.text or update.channel_post.caption or "(Medyalı mesaj)"
        print("Telegram mesajı:", text)
        asyncio.run(send_to_discord(text))

# Discord botunu ayrı bir thread'de başlat
threading.Thread(target=run_discord_bot).start()

# Telegram botunu başlat
updater = Updater(TELEGRAM_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.all, forward_channel_post))
updater.start_polling()
updater.idle()
