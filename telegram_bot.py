import os
import tempfile
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from discord_runner import send_to_discord

async def forward_any_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.channel_post or update.message
    if not msg:
        print("Mesaj alınamadı.")
        return

    print("Mesaj alındı.")
    text = msg.caption or msg.text or "(Boş mesaj)"
    print("Metin:", text)

    file = None
    original_filename = None

    if msg.photo:
        print("Fotoğraf bulundu.")
        file = await msg.photo[-1].get_file()
        original_filename = file.file_path.split('/')[-1] + ".jpg"
    elif msg.video:
        print("Video bulundu.")
        file = await msg.video.get_file()
        original_filename = file.file_path.split('/')[-1] + ".mp4"
    elif msg.document:
        print("Belge bulundu.")
        file = await msg.document.get_file()
        original_filename = msg.document.file_name  # gerçek dosya adı
    elif msg.audio:
        print("Ses bulundu.")
        file = await msg.audio.get_file()
        original_filename = msg.audio.file_name or "audio.ogg"
    elif msg.voice:
        print("Sesli mesaj bulundu.")
        file = await msg.voice.get_file()
        original_filename = "voice.ogg"

    if file:
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            file_path = temp.name
        await file.download_to_drive(file_path)
        print(f"Medya indirildi: {file_path} → {original_filename}")
        print("Discord'a medya gönderiliyor...")
        await send_to_discord(text, media_path=file_path, original_filename=original_filename)
        os.remove(file_path)
    else:
        print("Sadece metin gönderiliyor...")
        await send_to_discord(text)
