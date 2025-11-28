# backend/fastapi-ai/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import logging
import os
from pathlib import Path

# routers & services
from app.routes.auth import router as auth_router
from app.routes import recommend, dataset
from app.routes.users import router as users_router

# DB helper (safe init)
from app.database import init_db

# ML services (your own modules)
from app.services.ml_engine import MLEngine
from app.services.dataset_processor import DatasetProcessor

# logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("app.main")

app = FastAPI(
    title="AI Fashion Recommendation API",
    description="AI-powered fashion recommendation engine with embeddings and ML",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# service placeholders
ml_engine: MLEngine | None = None
dataset_processor: DatasetProcessor | None = None


@app.on_event("startup")
async def startup_event():
    global ml_engine, dataset_processor

    logger.info("Starting AI Fashion Recommendation API...")

    # attempt DB init but don't crash app if DB is unreachable
    ok = init_db(create_tables=True, raise_on_error=False)
    if not ok:
        logger.warning(
            "Database init failed — app will continue running but DB-backed endpoints will fail until DB is reachable."
        )
    else:
        logger.info("Database initialized successfully.")

    # Initialize ML services (non-fatal errors are caught and logged)
    try:
        ml_engine = MLEngine()
        dataset_processor = DatasetProcessor()

        models_dir = Path("models")
        if models_dir.exists():
            # load_models is async in your original code, so we await it
            await ml_engine.load_models(models_dir)
            logger.info("Pre-trained models loaded successfully.")
        else:
            logger.warning("No pre-trained models found. Will train or prepare on first use.")
    except Exception as e:
        logger.exception("Failed to initialize ML services: %s", e)


# routers
app.include_router(recommend.router, prefix="/api/ai", tags=["recommendations"])
app.include_router(dataset.router, prefix="/api/ai", tags=["dataset"])
app.include_router(auth_router, prefix="/api/auth")
app.include_router(users_router, prefix="/api/user")


@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "fashion-ai-recommendation",
        "version": "1.0.0",
        "features": [
            "NLP Matching",
            "K-Means Clustering",
            "Embeddings Generation",
            "Dataset Processing"
        ]
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "ml_engine_ready": ml_engine is not None,
        "dataset_processor_ready": dataset_processor is not None
    }


# Static files for serving images if present
static_dir = Path("static")
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


if __name__ == "__main__":
    import uvicorn

    # pick PORT from env (Render/Render-like platforms provide $PORT). fallback to 8000 locally.
    port_env = os.getenv("PORT", "8000")
    try:
        port = int(port_env)
    except ValueError:
        logger.warning("Invalid PORT env var %r — falling back to 8000", port_env)
        port = 8000

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        reload=False,  # disable reload in prod containers
        log_level="info"
    )
