FROM python:3.13-slim

WORKDIR /app

COPY data_collector/requirements.txt .

COPY data_collector/ .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python", "dataCollector.py"]