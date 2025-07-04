from typing import List
from sqlalchemy.orm import Session

from src.app.crud.recommendation import get_all_recommendations, create_recommendation, get_recommendation, \
    update_recommendation, delete_recommendation
from src.app.schemas.recommendation import RecommendationRead, RecommendationCreate


class RecommendationService:
    def list(self, db: Session) -> List[RecommendationRead]:
        return get_all_recommendations(db)

    def get(self, db: Session, rec_id: int) -> RecommendationRead:
        return get_recommendation(db, rec_id)

    def create(self, db: Session, rec: RecommendationCreate) -> RecommendationRead:
        return create_recommendation(db, rec)

    def update(self, db: Session, rec_id: int, rec: RecommendationCreate) -> RecommendationRead:
        return update_recommendation(db, rec_id, rec)

    def delete(self, db: Session, rec_id: int):
        return delete_recommendation(db, rec_id)
