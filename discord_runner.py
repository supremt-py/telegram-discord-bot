import os
import asyncio
import discord

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f"Discord bot aktif: {client.user}")

async def send_to_discord(text):
    await client.wait_until_ready()
    try:
        channel = client.get_channel(DISCORD_CHANNEL_ID)
        if channel:
            await channel.send(text)
        else:
            print("Hedef Discord kanalı bulunamadı.")
    except Exception as e:
        print(f"Discord'a mesaj gönderilirken hata oluştu: {e}")
