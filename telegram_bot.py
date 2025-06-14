import os
import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
    DeletedMessageHandler,
    EditedMessageHandler
)
from discord_runner import send_to_discord, telegram_to_discord, bot
from langdetect import detect


def is_only_turkish(text):
    try:
        return detect(text) == 'tr'
    except:
        return False


async def forward_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        text = update.channel_post.text or update.channel_post.caption or "(Medyalı mesaj)"
        msg_id = update.channel_post.message_id
        print("Telegram mesajı:", text)
        if is_only_turkish(text):
            await send_to_discord(text, telegram_msg_id=msg_id)


async def handle_deleted_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_id = update.channel_post.message_id
    discord_msg_id = telegram_to_discord.get(msg_id)
    if discord_msg_id:
        channel = bot.get_channel(int(os.getenv("DISCORD_CHANNEL_ID")))
        try:
            msg = await channel.fetch_message(discord_msg_id)
            await msg.delete()
        except Exception as e:
            print(f"Silme hatası: {e}")


async def handle_edited_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.edited_channel_post.text or update.edited_channel_post.caption or "(Medyalı düzenleme)"
    msg_id = update.edited_channel_post.message_id
    print("Telegram düzenleme:", text)
    if is_only_turkish(text):
        discord_msg_id = telegram_to_discord.get(msg_id)
        if discord_msg_id:
            channel = bot.get_channel(int(os.getenv("DISCORD_CHANNEL_ID")))
            try:
                msg = await channel.fetch_message(discord_msg_id)
                await msg.edit(content=text)
            except Exception as e:
                print(f"Güncelleme hatası: {e}")


def start_telegram_bot():
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, forward_channel_post))
    app.add_handler(EditedMessageHandler(handle_edited_message))
    app.add_handler(DeletedMessageHandler(handle_deleted_message))
    app.run_polling()
