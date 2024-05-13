FROM python:3.11.1-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY process_file_format.py .

COPY templates templates
COPY static static


CMD [ "python", "app.py" ]