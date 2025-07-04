from pydantic import BaseModel, Field

class RecommendationBase(BaseModel):
    titulo: str = Field(..., min_length=1)
    genero: str = Field(..., min_length=1)
    puntaje: int = Field(..., ge=1, le=10)
    comentario: str
    vista: bool = False

class RecommendationCreate(RecommendationBase):
    pass

class RecommendationRead(RecommendationBase):
    id: int

    class Config:
        orm_mode = True
