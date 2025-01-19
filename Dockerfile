
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
# Specify compatible versions for motor and pymongo
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir motor==3.1 pymongo==3.12.3 python-telegram-bot==20.3

# Expose the port the app runs on (if applicable)
EXPOSE 8000

# Run the application
CMD ["python", "bot.py"]
