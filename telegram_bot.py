import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from discord_runner import send_to_discord

async def forward_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        text = update.channel_post.text or update.channel_post.caption or "(Medyalı mesaj)"
        msg_id = update.channel_post.message_id
        print("Telegram mesajı:", text)
        asyncio.create_task(send_to_discord(text, telegram_msg_id=msg_id))  # DOĞRU SATIR

def start_telegram_bot():
    print("Telegram bot başlatılıyor...")
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, forward_channel_post))
    app.run_polling()
