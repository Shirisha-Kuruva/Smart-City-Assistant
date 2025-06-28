from pydantic import BaseSettings

class Settings(BaseSettings):
    WATSONX_API_KEY: str
    PROJECT_ID: str
    MODEL_ID: str
    PINECONE_API_KEY: str
    PINECONE_ENV: str

    class Config:
        env_file = ".env"

settings = Settings()
