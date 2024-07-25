FROM python:3.10-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y wget unzip  \
    wget \
    curl \
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
    libcurl4 \ 
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && apt-get install -y ./google-chrome-stable_current_amd64.deb \
  && rm -rf ./google-chrome-stable_current_amd64.deb

# Install ChromeDriver (replace with your desired version)
RUN wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
  && unzip chromedriver_linux64.zip && rm -rf chromedriver_linux64.zip \
  && mv chromedriver /usr/local/bin \
  && chmod +x /usr/local/bin/chromedriver

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Start Xvfb
RUN echo '#!/bin/bash\n\
Xvfb :99 -screen 0 1280x1024x24 &\n\
export DISPLAY=:99\n\
exec "$@"' > /usr/local/bin/start-xvfb.sh \
    && chmod +x /usr/local/bin/start-xvfb.sh

# Command to start the application
CMD ["/usr/local/bin/start-xvfb.sh", "python", "main.py"]
