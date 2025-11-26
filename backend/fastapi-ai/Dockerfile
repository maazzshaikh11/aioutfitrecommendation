# backend/fastapi-ai/Dockerfile
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# system deps needed to build/consume numpy/scipy/sklearn/faiss/psycopg2
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

# copy requirements first for caching
COPY requirements.txt .

# upgrade pip/setuptools/wheel and prefer binary wheels
RUN python -m pip install --upgrade pip setuptools wheel cython \
 && pip install --no-cache-dir --prefer-binary -r requirements.txt

# copy app
COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
