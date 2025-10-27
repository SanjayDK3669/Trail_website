FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# system deps for mysql driver
RUN apt-get update && apt-get install -y build-essential default-libmysqlclient-dev gcc --no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app
COPY gunicorn_conf.py /app/gunicorn_conf.py

ENV FLASK_APP=app
ENV FLASK_ENV=production

EXPOSE 8000

CMD ["gunicorn", "-c", "gunicorn_conf.py", "app.__init__:create_app()"]
