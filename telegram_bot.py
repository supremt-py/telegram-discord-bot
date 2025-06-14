import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from discord_runner import send_to_discord

from telegram.constants import MessageEntityType

async def forward_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post

    text = message.text or message.caption
    file_id = None

    # Fotoğraf gönderildiyse
    if message.photo:
        file_id = message.photo[-1].file_id  # En yüksek çözünürlükte olanı al

    # Video gönderildiyse
    elif message.video:
        file_id = message.video.file_id

    # Belge gönderildiyse
    elif message.document:
        file_id = message.document.file_id

    if file_id:
        file = await context.bot.get_file(file_id)
        file_path = await file.download_to_drive()
        print("Telegram dosyası indirildi:", file_path)

        # Dosya ile birlikte Discord'a gönder
        await send_to_discord(text or "(Dosya)", file_path=file_path)
    elif text:
        print("Telegram mesajı:", text)
        await send_to_discord(text)


async def start_telegram_bot():
    print("Telegram bot başlatılıyor...")
    token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.ALL, forward_channel_post))
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
