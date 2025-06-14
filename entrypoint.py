import threading
from telegram_bot import start_telegram_bot
from discord_runner import run_discord_bot

# Discord botu ayrı thread'de
threading.Thread(target=run_discord_bot).start()

# Telegram botu main thread'de
start_telegram_bot()
