from pydantic_settings import BaseSettings  

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    PROJECT_NAME: str = "Freelance Management System"
    
    class Config:
        env_file = ".env"

settings = Settings()