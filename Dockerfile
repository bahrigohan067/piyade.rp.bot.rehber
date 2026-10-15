FROM python:3.11-slim

WORKDIR /app

# Voice ve FFmpeg bağımlılıklarını yükle
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    libopus0 \
    libopus-dev \
    libffi-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
