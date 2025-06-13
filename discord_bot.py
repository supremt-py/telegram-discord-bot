import discord
import asyncio

DISCORD_TOKEN = 'MTM4MzA2NTYzNDc0MDUwMjU2OA.GtkoL0.oBa8ziGojW7D3iLMgx_AvfhVzl00SPiiNAUZ2E'
CHANNEL_ID = int('1336869450640523374')  # sadece rakam olacak

client = discord.Client(intents=discord.Intents.default())

async def send_to_discord(text):
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(text)

def run_discord_bot():
    asyncio.run(client.start(DISCORD_TOKEN))
