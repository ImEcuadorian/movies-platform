from fastapi import FastAPI

from src.app.core.config import settings
from src.app.db.base import Base
from src.app.db.session import engine
from src.app.api.v1.recommendation import router as rec_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(rec_router, prefix="/api/v1")
