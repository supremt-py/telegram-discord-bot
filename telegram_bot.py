import os
import asyncio
from telegram.ext import Updater, MessageHandler, Filters
from discord_runner import send_to_discord

def forward_channel_post(update, context):
    if update.channel_post:
        text = update.channel_post.text or update.channel_post.caption or "(Medyalı mesaj)"
        print("Telegram mesajı:", text)
        try:
            asyncio.run_coroutine_threadsafe(send_to_discord(text), asyncio.get_running_loop())
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(send_to_discord(text))

def start_telegram_bot():
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.all, forward_channel_post))
    updater.start_polling()
    updater.idle()
