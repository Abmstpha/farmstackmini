from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    PROJECT_NAME: str
    VERSION: str
    MONGODB_URI: str
    MONGODB_DB_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()
