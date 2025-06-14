import asyncio
from telegram_bot import start_telegram_bot
from discord_runner import start_discord_bot  # client değil

async def main():
    asyncio.create_task(start_discord_bot())  # Discord botu arka planda
    await asyncio.to_thread(start_telegram_bot)  # Telegram polling

if __name__ == "__main__":
    asyncio.run(main())
