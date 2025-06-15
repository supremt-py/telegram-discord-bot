import os
import tempfile
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from discord_runner import send_to_discord

# Kendi özel filtremiz: Sadece kanal mesajları
def is_channel_post(update: Update) -> bool:
    return update.channel_post is not None

async def forward_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.channel_post
    if not msg:
        print("Mesaj alınamadı.")
        return

    print("Kanal mesajı alındı.")
    text = msg.caption or msg.text or "(Boş mesaj)"
    print("Metin:", text)

    file = None
    if msg.photo:
        print("Fotoğraf bulundu.")
        file = await msg.photo[-1].get_file()
    elif msg.video:
        print("Video bulundu.")
        file = await msg.video.get_file()
    elif msg.document:
        print("Belge bulundu.")
        file = await msg.document.get_file()

    if file:
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            file_path = temp.name
        await file.download_to_drive(file_path)
        print(f"Medya indirildi: {file_path}")
        print("Discord'a medya gönderiliyor...")
        await send_to_discord(text, media_path=file_path)
        os.remove(file_path)
    else:
        print("Sadece metin gönderiliyor...")
        await send_to_discord(text)

async def start_telegram_bot():
    print("Telegram bot başlatılıyor...")
    token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()

    # Özel filtre fonksiyonu ile sadece kanal postlarını dinle
    app.add_handler(MessageHandler(filters.ALL & filters.UpdateType.MESSAGE, forward_channel_post, block=False), group=0)
    app.add_handler(MessageHandler(filters.ALL, forward_channel_post, block=False), group=1)
    app.add_handler(MessageHandler(filters.ALL, forward_channel_post, block=True), group=2)
    app.add_handler(MessageHandler(filters.BaseFilter(is_channel_post), forward_channel_post))

    await app.initialize()
    await app.start()
