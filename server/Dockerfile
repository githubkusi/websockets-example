FROM python:3.8-slim-buster
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY server.py .
CMD ["python3", "server.py"]

