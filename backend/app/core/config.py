from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    qdrant_host: str
    qdrant_port: int
    
    collection_name: str = "documents"
    
    embedding_model: str
    embedding_service_url: str = "http://embedding-service:8001"
    
    llm_provider: str
    ollama_host: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )
    
settings = Settings()