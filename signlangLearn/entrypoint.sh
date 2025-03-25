#!/bin/bash

# Várakozás a PostgreSQL adatbázisra, hogy elérhetővé váljon
echo "Waiting for the database to be ready..."
until nc -z -v -w30 db 5432; do
  echo "Waiting for database connection..."
  sleep 1
done

# Ellenőrizzük, hogy a virtuális környezet létezik-e
if [ ! -d "/app/venv" ]; then
  echo "Virtual environment not found. Creating..."
  python3 -m venv /app/venv
fi

# Virtuális környezet aktiválása
source /app/venv/bin/activate

# Függőségek telepítése, ha még nem telepítettek
if [ ! -f "/app/venv/bin/django-admin" ]; then
  echo "Installing dependencies..."
  pip install --upgrade pip
  pip install -r /app/requirements.txt
fi

# Ha adatbázis migráció szükséges, azt futtatjuk
python /app/manage.py migrate

# Django fejlesztői szerver elindítása
python /app/manage.py runserver 0.0.0.0:8000
