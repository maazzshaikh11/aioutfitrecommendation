# backend/fastapi-ai/Dockerfile-conda
FROM mambaorg/micromamba:1.6.0

WORKDIR /app
COPY . /app

# create env, install via mamba/conda from conda-forge (fast, prebuilt)
RUN micromamba create -y -n app python=3.11 -c conda-forge \
     fastapi=0.104.1 uvicorn=0.24.0 sqlalchemy=2.0.23 \
     pydantic=2.5.0 python-dotenv=1.0.0 numpy=1.24.4 pandas=2.1.4 \
     scikit-learn=1.3.2 faiss-cpu=1.7.4 sentence-transformers=2.2.2 \
     pillow=10.1.0 imagehash requests openai httpx aiofiles python-multipart \
 && micromamba clean --all --yes

# activate env on container start
ENV PATH=/opt/conda/envs/app/bin:$PATH
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
