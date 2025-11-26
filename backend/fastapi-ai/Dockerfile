FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# system deps for numpy/scipy/sklearn/faiss/psycopg2
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

# copy requirements first for better cache
COPY backend/fastapi-ai/requirements.txt /tmp/requirements.txt

# upgrade pip & install (prefer binary wheels)
RUN python -m pip install --upgrade pip setuptools wheel cython \
 && pip install --no-cache-dir --prefer-binary -r /tmp/requirements.txt

# copy the app code and start script
COPY backend/fastapi-ai/ /app/

# ensure start script is executable
RUN chmod +x /app/start.sh

EXPOSE 8000

# CMD will be used by Render — start.sh expands $PORT at runtime
CMD ["/app/start.sh"]
