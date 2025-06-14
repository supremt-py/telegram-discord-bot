from telegram_bot import start_telegram_bot
from discord_runner import start_discord_bot

import threading

# Discord botunu ayrı thread'de çalıştır
threading.Thread(target=start_discord_bot).start()

# Telegram botunu başlat
start_telegram_bot()
