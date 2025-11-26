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

# copy requirements from THIS folder
COPY requirements.txt /tmp/requirements.txt

# upgrade pip/setuptools/wheel and prefer binary wheels
RUN python -m pip install --upgrade pip setuptools wheel cython \
 && pip install --no-cache-dir --prefer-binary -r /tmp/requirements.txt

# copy the app code (copies contents of backend/fastapi-ai into /app)
COPY . /app

# make sure start script is executable
RUN chmod +x /app/start.sh

EXPOSE 8000

# start via shell so env var expansion works and logs show properly
CMD ["sh", "-c", "/app/start.sh"]
