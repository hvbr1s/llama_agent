FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git && rm -rf /var/cache/apt/archives /var/lib/apt/lists
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir wheel && pip install --no-cache-dir -r requirements.txt
COPY . /app
CMD [ "uvicorn", "app:app", "--port", "80", "--host", "0.0.0.0" ]
