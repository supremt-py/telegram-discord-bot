import os
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from discord_runner import send_to_discord_file

async def forward_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post
    if not message:
        return

    if message.photo:  # Fotoğraf varsa
        file_id = message.photo[-1].file_id  # En yüksek çözünürlükteki fotoğraf
        file = await context.bot.get_file(file_id)
        file_path = "/tmp/temp_photo.jpg"
        await file.download_to_drive(file_path)
        caption = message.caption or "Fotoğraf"
        print("Telegram mesajı: [Fotoğraf] " + caption)
        await send_to_discord_file(file_path, caption)

    elif message.text:
        print("Telegram mesajı:", message.text)
        await send_to_discord_file(None, message.text)
