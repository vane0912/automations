ARG PORT=443
FROM cypress/browsers:latest

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the environment variable PATH
ENV PATH /home/root/.local/bin:${PATH}

# Expose the port
EXPOSE $PORT

# Command to run the application
CMD uvicorn main:app --host 0.0.0.0 --port $PORT