FROM python:3.11-slim

# Системные зависимости для psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev gcc bash postgresql-client && \
    pip install --upgrade pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем проект
COPY ./src /app

# Копируем entrypoint и даём права
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Указываем команду Gunicorn через $PORT
CMD ["gunicorn", "dds_project.wsgi:application", "--bind", "0.0.0.0:$PORT"]
