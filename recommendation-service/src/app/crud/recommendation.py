from sqlalchemy.orm import Session

from src.app.models.recommendation import Recommendation
from src.app.schemas.recommendation import RecommendationCreate


def get_all_recommendations(db: Session):
    return db.query(Recommendation).all()

def get_recommendation(db: Session, rec_id: int):
    return db.query(Recommendation).filter(Recommendation.id == rec_id).first()

def create_recommendation(db: Session, rec: RecommendationCreate):
    db_rec = Recommendation(**rec.dict())
    db.add(db_rec)
    db.commit()
    db.refresh(db_rec)
    return db_rec

def update_recommendation(db: Session, rec_id: int, rec: RecommendationCreate):
    db_rec = get_recommendation(db, rec_id)
    if not db_rec:
        return None
    for field, value in rec.dict().items():
        setattr(db_rec, field, value)
    db.commit()
    db.refresh(db_rec)
    return db_rec

def delete_recommendation(db: Session, rec_id: int):
    db_rec = get_recommendation(db, rec_id)
    if not db_rec:
        return None
    db.delete(db_rec)
    db.commit()
    return db_rec
