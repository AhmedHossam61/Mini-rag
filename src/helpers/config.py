from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "mini-rag"
    app_version: str = "0.0.1"
    class Config:
        env_file = ".env"
        