ARG PORT=443

# Use a suitable base image with Python 3 already installed
FROM cypress/browsers:latest

# Install Python 3 and necessary tools
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    python3 -m pip install --upgrade pip

# Set working directory in the container
WORKDIR /app

# Copy requirements.txt file
COPY requirements.txt .

# Install dependencies
RUN python3 -m pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port your app runs on
EXPOSE $PORT

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]