import threading
from telegram_bot import start_telegram_bot
from discord_runner import run_discord_bot

# Discord botunu ayrı thread'de başlat
threading.Thread(target=run_discord_bot).start()

# Telegram botu ana thread'de çalışır
start_telegram_bot()
