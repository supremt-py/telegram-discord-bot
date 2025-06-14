from telegram_bot import start_telegram_bot
from discord_runner import bot
import threading
import os  # ← eksik olan bu satırdı

# Discord botunu ayrı thread'de başlat
threading.Thread(target=bot.run, args=(os.getenv("DISCORD_TOKEN"),)).start()

# Telegram botunu başlat
start_telegram_bot()
