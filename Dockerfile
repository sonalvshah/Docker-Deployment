FROM python:3.9-slim

WORKDIR /app

COPY script.py .

COPY data/ /home/data/

CMD ["python", "script.py"]