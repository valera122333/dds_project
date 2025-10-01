#!/bin/bash
set -e

# Ждём пока Postgres станет доступен
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
  echo "ждем загрузку бд"
  sleep 2
done

echo "применяем миграции..."
python manage.py makemigrations
python manage.py migrate --noinput

# логин пас админа
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    python manage.py createsuperuser --noinput || true
fi

echo "сбор статики"
python manage.py collectstatic --noinput

 
exec "$@"
