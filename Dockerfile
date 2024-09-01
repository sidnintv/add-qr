# Using the official Python image
FROM python:3.12-slim

# We install the necessary dependencies
RUN pip install --no-cache-dir pillow qrcode[pil] moviepy

# Specifying the working directory inside the container
WORKDIR /app

# Copy the script to the container
COPY add_qr.py .

# Specify the default command
CMD ["python", "add_qr.py"]
