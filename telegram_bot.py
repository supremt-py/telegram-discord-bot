import os
import aiohttp
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from discord import File
from discord_runner import send_to_discord, bot

async def download_file(file_url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as resp:
            if resp.status == 200:
                with open(filename, 'wb') as f:
                    f.write(await resp.read())
                return filename
    return None

async def forward_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        file = None
        text = update.channel_post.caption or update.channel_post.text or "(Boş mesaj)"

        # Eğer medya varsa dosyayı al
        if update.channel_post.photo:
            file = await context.bot.get_file(update.channel_post.photo[-1].file_id)
        elif update.channel_post.document:
            file = await context.bot.get_file(update.channel_post.document.file_id)
        elif update.channel_post.video:
            file = await context.bot.get_file(update.channel_post.video.file_id)

        if file:
            file_path = f"/tmp/{file.file_id}"
            await file.download_to_drive(file_path)
            discord_file = File(file_path, filename="dosya")
            await send_to_discord(text, discord_file)
            os.remove(file_path)
        else:
            await send_to_discord(text)

async def start_telegram_bot():
    print("Telegram bot başlatılıyor...")
    token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.ALL, forward_channel_post))
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
