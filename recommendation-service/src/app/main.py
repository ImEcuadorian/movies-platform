from fastapi import FastAPI
from src.app.core.config import settings
from src.app.db.session import engine
from src.app.db.base import Base
from src.app.api.v1.recommendation import router as rec_router

# Crea esquemas al arrancar
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/health", include_in_schema=False)
async def health_check():
    return {"status": "ok"}

app.include_router(rec_router, prefix="/api/v1")
