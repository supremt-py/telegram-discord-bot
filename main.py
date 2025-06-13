from telegram.ext import Updater, MessageHandler, Filters
import threading
from discord_bot import run_discord_bot, send_to_discord
import asyncio

TELEGRAM_TOKEN = '7504590949:AAGF-8ac2Q7gsxGxi6mfJ9zG04oURlzMKr4'

def forward_channel_post(update, context):
    if update.channel_post:
        text = update.channel_post.text or update.channel_post.caption or "(Medyalı mesaj)"
        print("Telegram mesajı:", text)
        asyncio.run(send_to_discord(text))

threading.Thread(target=run_discord_bot).start()

updater = Updater(TELEGRAM_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.all, forward_channel_post))
updater.start_polling()
updater.idle()
