# Use Railway's base Python image
FROM railwayapp/python:3.10

# Install Python and dependencies
RUN apt-get update \
    && apt-get install -y python3-pip \
    && pip install --upgrade pip

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT}"]