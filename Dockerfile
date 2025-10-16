# Eng barqaror Python image
FROM python:3.11-slim

# Ishchi papka
WORKDIR /app

# Matplotlib va boshqa liblar uchun kerakli system kutubxonalar
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc g++ libffi-dev libssl-dev libjpeg-dev zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

# Kutubxonalarni o‘rnatish
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Foylalarni konteynerga ko‘chirish
COPY . .

# Ishga tushirish buyrug‘i
CMD ["python", "bot.py"]
