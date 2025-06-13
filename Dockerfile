# Python 3.10 bazlı bir imaj kullan
FROM python:3.10-slim

# Gerekli sistem paketlerini yükle
RUN apt-get update && apt-get install -y build-essential

# Çalışma dizinini ayarla
WORKDIR /app

# Kod dosyalarını kopyala
COPY . .

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı başlat
CMD ["python", "main.py"]
