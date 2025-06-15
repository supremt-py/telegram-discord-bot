import os
import tempfile
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from discord_runner import send_to_discord

async def forward_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.channel_post
    if not msg:
        return  # Sadece kanal mesajlarını işle

    text = msg.caption or msg.text or "(Boş mesaj)"
    file = None

    if msg.photo:
        file = await msg.photo[-1].get_file()
    elif msg.video:
        file = await msg.video.get_file()
    elif msg.document:
        file = await msg.document.get_file()

    if file:
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            file_path = temp.name
        await file.download_to_drive(file_path)
        print(f"Medya indirildi: {file_path}")
        await send_to_discord(text, media_path=file_path)
        os.remove(file_path)
    else:
        print(f"Metin gönderiliyor: {text}")
        await send_to_discord(text)

async def start_telegram_bot():
    print("Telegram bot başlatılıyor...")
    token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()

    # ALL filtrele, ama sadece channel_post kontrol et
    app.add_handler(MessageHandler(filters.ALL, forward_channel_post))

    await app.initialize()
    await app.start()
