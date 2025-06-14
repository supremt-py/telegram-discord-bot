from telegram_bot import start_telegram_bot
from discord_runner import bot
import threading
import os

# Discord botunu ayrı thread’de başlat
threading.Thread(target=bot.run, args=(os.getenv("DISCORD_TOKEN"),)).start()

# Telegram botunu ana akışta başlat
start_telegram_bot()
