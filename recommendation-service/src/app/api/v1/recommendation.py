from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.app.db.session import SessionLocal
from src.app.schemas.recommendation import RecommendationRead, RecommendationCreate
from src.app.services.recommendation_service import RecommendationService

router = APIRouter(prefix="/recommendations", tags=["recommendations"])
service = RecommendationService()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[RecommendationRead])
def read_recommendations(db: Session = Depends(get_db)):
    return service.list(db)

@router.get("/{rec_id}", response_model=RecommendationRead)
def read_recommendation(rec_id: int, db: Session = Depends(get_db)):
    rec = service.get(db, rec_id)
    if not rec:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No encontrada")
    return rec

@router.post("/", response_model=RecommendationRead, status_code=status.HTTP_201_CREATED)
def create_recommendation(rec: RecommendationCreate, db: Session = Depends(get_db)):
    return service.create(db, rec)

@router.put("/{rec_id}", response_model=RecommendationRead)
def update_recommendation(rec_id: int, rec: RecommendationCreate, db: Session = Depends(get_db)):
    updated = service.update(db, rec_id, rec)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No encontrada")
    return updated

@router.delete("/{rec_id}", response_model=RecommendationRead)
def delete_recommendation(rec_id: int, db: Session = Depends(get_db)):
    deleted = service.delete(db, rec_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No encontrada")
    return deleted
