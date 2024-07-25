FROM python:3.10

# Install essential packages
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

# Install Chrome browser
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin \
    && rm /tmp/chromedriver.zip \
    && chmod +x /usr/bin/chromedriver

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV PATH="$PATH:/bin:/usr/bin"

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
