# backend/fastapi-ai/app/database.py
import os
import logging
from dotenv import load_dotenv

from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

logger = logging.getLogger("database")

# prefer env var DATABASE_URL (set this in Render / Render Postgres external URL)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://ai_user:ai_password@localhost:5432/fashion_ai"
)

# engine (tune pool sizes if needed)
engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    pool_recycle=300
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db(create_tables: bool = False, raise_on_error: bool = False) -> bool:
    """
    Try a quick DB connection check and optionally create tables.
    Returns True if DB reachable (and tables created when requested), otherwise False.
    If raise_on_error=True, re-raises exceptions to fail startup.
    """
    try:
        # use sqlalchemy.text(...) to make an executable object
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            conn.commit()  # ensure any transactional checks are finished

        if create_tables:
            Base.metadata.create_all(bind=engine)
            logger.info("Created tables (if not exist).")

        return True

    except Exception as exc:
        logger.exception("Database initialization failed: %s", exc)
        if raise_on_error:
            raise
        return False


# dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
