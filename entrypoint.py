import threading
import os
from telegram_bot import start_telegram_bot
from discord_runner import client

# Discord botu ayrı thread’de başlat
threading.Thread(target=client.run, args=(os.getenv("DISCORD_TOKEN"),)).start()

# Telegram botunu başlat
start_telegram_bot()
