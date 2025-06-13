import os
from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters
import asyncio
from discord_bot import send_to_discord

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def forward_channel_post(update, context):
    if update.channel_post:
        text = update.channel_post.text or update.channel_post.caption or "(Medyalı mesaj)"
        print("Telegram mesajı:", text)
        asyncio.run(send_to_discord(text))

updater = Updater(TELEGRAM_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.all, forward_channel_post))
updater.start_polling()
updater.idle()
