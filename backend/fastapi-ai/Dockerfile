# backend/fastapi-ai/Dockerfile
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# system deps needed to build many scientific packages
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

# copy requirements and install them (cache layer)
COPY backend/fastapi-ai/requirements.txt /tmp/requirements.txt

# upgrade pip/setuptools/wheel for better binary wheel handling
RUN python -m pip install --upgrade pip setuptools wheel cython \
 && pip install --no-cache-dir --prefer-binary -r /tmp/requirements.txt

# copy app sources
COPY backend/fastapi-ai/ /app/

# expose (optional)
EXPOSE 8000

# Start via shell so $PORT expands. If PORT not set, use 8000.
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --proxy-headers"]
