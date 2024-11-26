FROM python:3.13-slim

WORKDIR /app

COPY server/requirements.txt .

COPY server/ .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python", "server.py"]