FROM python:3.10

# Install essential packages
RUN apt-get update && apt-get install -y \
    wget \
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

# Install Chrome browser
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# Fetch the latest stable version of ChromeDriver and install
RUN set -eux; \
    RESPONSE=$(curl -sSL "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions.json") \
    && LATEST_STABLE_VERSION=$(echo "$RESPONSE" | grep -oP '"Stable":\s*\{\s*"channel":.*?"version":\s*"\K[^"]+') \
    && CHROMEDRIVER_URL="https://storage.googleapis.com/chrome-for-testing-public/${LATEST_STABLE_VERSION}/linux64/chromedriver_linux64.zip" \
    && echo "Downloading ChromeDriver from $CHROMEDRIVER_URL" \
    && curl -sSL "$CHROMEDRIVER_URL" -o /tmp/chromedriver_linux64.zip \
    && echo "Downloaded file size: $(du -h /tmp/chromedriver_linux64.zip | cut -f1)" \
    && unzip -q /tmp/chromedriver_linux64.zip -d /usr/local/bin \
    && rm /tmp/chromedriver_linux64.zip \
    && chmod +x /usr/local/bin/chromedriver

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV PATH="$PATH:/bin:/usr/bin:/usr/local/bin"

# Clean up webdriver_manager files
RUN rm -rf /root/.wdm*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["python", "main.py"]
