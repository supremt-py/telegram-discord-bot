import asyncio
from telegram_bot import start_telegram_bot


from discord_runner import start_discord_bot

async def main():
    discord_task = asyncio.create_task(start_discord_bot())
    telegram_task = asyncio.create_task(start_telegram_bot())
    await asyncio.gather(discord_task, telegram_task)

if __name__ == "__main__":
    asyncio.run(main())
