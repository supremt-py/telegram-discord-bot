from telegram_bot import start_telegram_bot
from discord_runner import bot
import threading
import os

threading.Thread(target=bot.run, args=(os.getenv("DISCORD_TOKEN"),)).start()
start_telegram_bot()
