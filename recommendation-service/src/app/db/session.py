from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=20, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
