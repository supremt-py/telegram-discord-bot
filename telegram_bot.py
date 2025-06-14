import os
import aiohttp
import tempfile
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from discord_runner import send_to_discord

async def download_file(url: str, file_path: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                with open(file_path, 'wb') as f:
                    f.write(await resp.read())

async def forward_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        text = update.channel_post.caption or update.channel_post.text or "(Boş mesaj)"
        file_path = None

        if update.channel_post.photo:
            file = await context.bot.get_file(update.channel_post.photo[-1].file_id)
        elif update.channel_post.video:
            file = await context.bot.get_file(update.channel_post.video.file_id)
        elif update.channel_post.document:
            file = await context.bot.get_file(update.channel_post.document.file_id)
        else:
            file = None

        if file:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                await download_file(file.file_path, tmp_file.name)
                file_path = tmp_file.name

        print("Telegram mesajı:", text)
        await send_to_discord(text, file_path)

async def start_telegram_bot():
    print("Telegram bot başlatılıyor...")
    token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.ALL, forward_channel_post))
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
