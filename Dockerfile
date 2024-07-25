FROM python:3.10

# Install necessary packages
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
    --no-install-recommends

RUN CHROME_SETUP=google-chrome.deb && \
wget -O $CHROME_SETUP "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" && \
dpkg -i $CHROME_SETUP && \
# apt install $CHROME_SETUP && \
apt-get install -y -f && \
rm $CHROME_SETUP
# Install ChromeDriver
RUN CHROMEDRIVER_VERSION=111.0.5563.64 && \
    wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/bin && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip

# Set working directory
WORKDIR /app

COPY . .
# Copy requirements and install Python dependencies
RUN pip3 install -r requirements.txt
# Copy the rest of the application code

# Command to run the application
CMD ["python", "main.py"]
