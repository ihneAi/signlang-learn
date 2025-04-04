FROM python:3.12.8-slim

WORKDIR /app

# Requirements telepítése
COPY requirements.txt .
RUN pip install -r requirements.txt


COPY jelapp .

# Port kinyitása
EXPOSE 8001

# Alapértelmezett karakterkódolás
ENV LANG C.UTF-8

# Környezeti változók beállítása (adatbázis elérhetőségek)
ENV DATABASE_HOST=db
ENV DATABASE_PORT=5432
ENV DATABASE_NAME=signlang_db
ENV DATABASE_USER=signlang_user
ENV DATABASE_PASSWORD=strongpassword123

# Alkalmazás indítása
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]