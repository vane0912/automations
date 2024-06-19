ARG PORT=443

# Use a suitable base image with Python 3 already installed
FROM cypress/browsers:latest

# Install Python 3 and necessary tools using apt-get (assuming Debian-based)
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip

# Set working directory in the container
WORKDIR /app

# Create a virtual environment and activate it
RUN python3 -m venv /opt/venv
ENV PATH /opt/venv/bin:$PATH

# Copy requirements.txt file
COPY requirements.txt .

# Install dependencies within the virtual environment
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port your app runs on
EXPOSE $PORT

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]
