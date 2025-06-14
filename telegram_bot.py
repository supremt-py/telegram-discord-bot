import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from discord_runner import send_to_discord

async def forward_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        text = update.channel_post.text or update.channel_post.caption or "(Medyalı mesaj)"
        print("Telegram mesajı:", text)
        await send_to_discord(text)

async def start_telegram_bot():
    print("Telegram bot başlatılıyor...")
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, forward_channel_post))

    # run_polling() yerine bunu kullan
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await app.updater.wait_until_shutdown()
