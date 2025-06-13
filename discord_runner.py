import os
import discord
import asyncio

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

client = discord.Client(intents=discord.Intents.default())

async def send_to_discord(text):
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(text)

def run_discord_bot():
    asyncio.run(client.start(DISCORD_TOKEN))
