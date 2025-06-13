import discord
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("MTM4MzA2NTYzNDc0MDUwMjU2OA.GtkoL0.oBa8ziGojW7D3iLMgx_AvfhVzl00SPiiNAUZ2E")
CHANNEL_ID = int(os.getenv("1336869450640523374"))

client = discord.Client(intents=discord.Intents.default())

async def send_to_discord(text):
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(text)

def run_discord_bot():
    asyncio.run(client.start(DISCORD_TOKEN))
