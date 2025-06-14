import asyncio
from telegram_bot import start_telegram_bot
from discord_runner import start_discord_bot

async def main():
    telegram_task = asyncio.to_thread(start_telegram_bot)
    discord_task = start_discord_bot()
    await asyncio.gather(telegram_task, discord_task)

if __name__ == "__main__":
    asyncio.run(main())
