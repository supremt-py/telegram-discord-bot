import asyncio
from telegram_bot import start_telegram_bot
from discord_runner import start_discord_bot

async def main():
    # Discord botu arka planda başlasın
    asyncio.create_task(start_discord_bot())

    # Telegram botu aynı event loop içinde
    await start_telegram_bot()

if __name__ == "__main__":
    asyncio.run(main())
