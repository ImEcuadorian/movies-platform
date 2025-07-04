from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Recommendation Service"
    SQLALCHEMY_DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()