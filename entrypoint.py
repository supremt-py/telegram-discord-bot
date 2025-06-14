import threading
import os
from telegram_bot import start_telegram_bot
from discord_runner import bot

# Discord botunu ayrı bir thread'de başlat
discord_token = os.getenv("DISCORD_TOKEN")
if not discord_token:
    print("HATA: DISCORD_TOKEN tanımlı değil!")
else:
    threading.Thread(target=bot.run, args=(discord_token,)).start()

# Telegram botunu başlat
start_telegram_bot()
