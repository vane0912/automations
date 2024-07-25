# Use the official Python image as a base
FROM python:3.10

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    curl \
    unzip \
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

# Install Google Chrome
RUN curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN CHROMEDRIVER_VERSION=127.0.6533.72 \
    && wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/$CHROMEDRIVER_VERSION/linux64/chromedriver-linux64.zip	 \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin \
    && rm /tmp/chromedriver.zip \
    && chmod +x /usr/local/bin/chromedriver

# Set up a working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
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
