from sqlalchemy import Column, Integer, String, Boolean

from src.app.db.base import Base

class Recommendation(Base):
    __tablename__ = "recommendations"

    id        = Column(Integer, primary_key=True, index=True)
    titulo    = Column(String, index=True)
    genero    = Column(String, index=True)
    puntaje   = Column(Integer)
    comentario= Column(String)
    vista     = Column(Boolean, default=False)
