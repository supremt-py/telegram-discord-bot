# Python imajı
FROM python:3.10

# Çalışma dizinini ayarla
WORKDIR /app

# Gerekli dosyaları kopyala
COPY . /app

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Ortam değişkenlerini destekle
ENV PYTHONUNBUFFERED=1

# Start komutu
CMD ["python", "entrypoint.py"]

discord_bot.py:
import discord
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Discord bot aktif: {client.user}")

async def send_to_discord(text):
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(text)
    else:
        print("Discord kanal bulunamadı.")

async def start_discord_bot():
    await client.start(DISCORD_TOKEN)
