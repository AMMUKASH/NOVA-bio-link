# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Expose port for aiohttp health server
EXPOSE 8080

# Default command
CMD ["python", "main.py"]
