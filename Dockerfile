# Use a lean Python base image
FROM python:3.10-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y \
    xvfb \
    libgbm1 \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libnspr4 \
    libnss3 \
    lsb-release \
    xdg-utils \
    libxss1 \
    libdbus-glib-1-2 \
    fonts-liberation \
    libu2f-udev \
    libvulkan1 \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Start Xvfb to run headless Chrome
RUN echo '#!/bin/bash\n\
Xvfb :99 -screen 0 1280x1024x24 &\n\
export DISPLAY=:99\n\
exec "$@"' > /usr/local/bin/start-xvfb.sh \
    && chmod +x /usr/local/bin/start-xvfb.sh

# Set the default command to start Xvfb and the application
CMD ["/usr/local/bin/start-xvfb.sh", "python", "main.py"]
