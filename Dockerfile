# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем необходимые зависимости
RUN pip install --no-cache-dir pillow qrcode[pil] moviepy

# Указываем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем скрипт в контейнер
COPY add_qr.py .

# Указываем команду по умолчанию
CMD ["python", "add_qr.py"]
