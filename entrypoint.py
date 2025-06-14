from telegram_bot import start_telegram_bot
from discord_runner import run_discord_bot
import threading

threading.Thread(target=run_discord_bot).start()
start_telegram_bot()
