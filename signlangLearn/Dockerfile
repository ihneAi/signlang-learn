FROM python:3.12.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8001

ENV LANG C.UTF-8

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
