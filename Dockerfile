# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Set environment variables as placeholders
# Actual values will be injected during GitHub Actions workflow
ENV LATITUDE="your_latitude"
ENV LONGITUDE="your_longitude"
ENV DISCORD_WEBHOOK_URL="your_discord_webhook_url"

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# --no-cache-dir: Disables the cache, which is useful for keeping image size down
# -r: Install from the given requirements file.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
# This includes main.py, call_api/, and marketing/ directories
COPY main.py .
COPY call_api/ ./call_api/
COPY marketing/ ./marketing/

# Define the command to run your application
CMD ["python", "main.py"]
