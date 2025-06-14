import asyncio
from telegram_bot import start_telegram_bot
from discord_runner import start_discord_bot

async def main():
    # Discord botunu arka planda başlat
    asyncio.create_task(start_discord_bot())

    # Telegram botunu aynı event loop içinde çalıştır
    await start_telegram_bot()

if __name__ == "__main__":
    asyncio.run(main())
