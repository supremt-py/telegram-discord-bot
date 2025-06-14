import discord
import os
import asyncio

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

client = discord.Client(intents=discord.Intents.default())
loop = asyncio.get_event_loop()

async def send_to_discord(text):
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(text)

def start_discord_bot():
    loop.create_task(client.start(DISCORD_TOKEN))
