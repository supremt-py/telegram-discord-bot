import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from discord_runner import send_to_discord  # Bu senkron gibi çalışacak artık

async def forward_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        text = update.channel_post.text or update.channel_post.caption or "(Medyalı mesaj)"
        print("Telegram mesajı:", text)
        send_to_discord(text)  # Artık sadece direkt çağırıyoruz, await veya create_task YOK

def start_telegram_bot():
    print("Telegram bot başlatılıyor...")
    token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.ALL, forward_channel_post))
    app.run_polling()
