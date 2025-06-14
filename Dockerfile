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
CMD ["python", "telegram_bot.py"]
