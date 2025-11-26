# backend/fastapi-ai/Dockerfile
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    gfortran \
    cmake \
    pkg-config \
    git \
    curl \
    wget \
    libpq-dev \
    libopenblas-dev \
    liblapack-dev \
    libblas-dev \
    libgomp1 \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python -m pip install --upgrade pip setuptools wheel cython \
 && pip install --no-cache-dir --prefer-binary -r requirements.txt

COPY . .

COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 8000

CMD ["/start.sh"]
