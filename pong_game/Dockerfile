# Stage 1: Base Python Setup
FROM python:3.7-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the project code into the container
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# NGINX configuration
RUN rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose the port for NGINX (80) and Daphne (8000)
EXPOSE 80 8000

# Start both NGINX and Daphne
CMD service nginx start && daphne -b 0.0.0.0 -p 8000 pong_game.asgi:application

