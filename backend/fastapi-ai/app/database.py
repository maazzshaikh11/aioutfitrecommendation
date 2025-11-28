# backend/fastapi-ai/app/database.py
import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()
logger = logging.getLogger("database")
logger.setLevel(logging.INFO)

# Read the DATABASE_URL env var (set this on Render to the External DB URL)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    # local dev fallback (sqlite) — safe when you don't have Postgres available
    "sqlite:///./dev_local.db",
)

# Helper: if using sqlite we need special connect args and default pooling
is_sqlite = DATABASE_URL.startswith("sqlite")

engine_kwargs = {
    "pool_pre_ping": True,
    "pool_recycle": 300,
}

# Only set pool_size / max_overflow for DBs that support it (Postgres etc.)
if not is_sqlite:
    engine_kwargs.update({"pool_size": 10, "max_overflow": 20})

if is_sqlite:
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        **engine_kwargs,
    )
else:
    engine = create_engine(
        DATABASE_URL,
        **engine_kwargs,
    )

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base for models
Base = declarative_base()


def get_db():
    """
    Dependency: yields a DB session; closes it after use.
    Use in FastAPI endpoints like:
        db = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db(create_tables: bool = True, raise_on_error: bool = False) -> bool:
    """
    Safe DB initialization helper.
    - Attempts to create tables (Base.metadata.create_all) if create_tables=True.
    - Returns True on success, False on failure.
    - On failure it logs the error and (by default) does NOT raise, so app startup won't crash.
    - If raise_on_error=True it will re-raise the exception.
    """
    if not create_tables:
        return True

    try:
        # Do a lightweight check before attempting to create_all: try connecting.
        with engine.connect() as conn:
            # optional lightweight check: select 1
            conn.execute("SELECT 1")
        # Create tables (idempotent)
        Base.metadata.create_all(bind=engine)
        logger.info("Database connected and tables created (if not present).")
        return True
    except Exception as exc:
        logger.exception("Database initialization failed: %s", exc)
        if raise_on_error:
            raise
        return False
