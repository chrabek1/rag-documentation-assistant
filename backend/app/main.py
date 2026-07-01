from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings

app = FastAPI(title="RAG Documentation Assistant API")

app.include_router(health_router)

@app.get("/config")
def show_config():
    return {
        "qdrant_host": settings.qdrant_host,
        "qdrant_port": settings.qdrant_port,
        "embedding_model": settings.embedding_model,
        "llm_provider": settings.llm_provider,
        "ollama_host": settings.ollama_host,
    }