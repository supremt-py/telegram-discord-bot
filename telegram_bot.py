import os
import tempfile
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from discord_runner import send_to_discord
import aiohttp

async def forward_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.channel_post

    if not msg:
        return

    text = msg.text or msg.caption or "(Boş mesaj)"
    file = None

    # Medya kontrolü ve indirme
    if msg.photo:
        file = await msg.photo[-1].get_file()
    elif msg.video:
        file = await msg.video.get_file()
    elif msg.document:
        file = await msg.document.get_file()
    elif msg.audio:
        file = await msg.audio.get_file()
    elif msg.voice:
        file = await msg.voice.get_file()

    if file:
        # Geçici dosya oluştur
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            file_path = temp.name
        await file.download_to_drive(file_path)
        print(f"Medya indirildi: {file_path}")
        await send_to_discord(text, media_path=file_path)
        os.remove(file_path)
    else:
        print("Sadece metin mesajı:", text)
        await send_to_discord(text)

async def start_telegram_bot():
    print("Telegram bot başlatılıyor...")
    token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.ALL, forward_channel_post))
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
