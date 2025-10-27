# Use a lightweight Python base image
FROM python:3.11-slim

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# ---- Install MySQL & Build Dependencies ----
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    libmariadb-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# ---- Copy requirements first (for caching) ----
COPY backend/requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy application code ----
COPY backend/app /app/app
COPY backend/gunicorn_conf.py /gunicorn_conf.py

# ---- Set environment variables ----
ENV FLASK_APP=app
ENV FLASK_ENV=production
ENV PORT=8000

# ---- Expose the port ----
EXPOSE 8000

# ---- Start the app using Gunicorn ----
CMD ["gunicorn", "-c", "gunicorn_conf.py", "app.__init__:create_app()"]
