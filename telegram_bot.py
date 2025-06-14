import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from discord_runner import send_to_discord_file

def forward_channel_post_sync(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Bu fonksiyon sadece metin için çalışır, medya için async versiyonunu yaparız
    message = update.channel_post
    if not message:
        return

    if message.text:
        print("Telegram mesajı:", message.text)
        context.application.create_task(send_to_discord_file(None, message.text))

def start_telegram_bot():
    print("Telegram bot başlatılıyor...")
    token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.ALL, forward_channel_post_sync))
    app.run_polling()
