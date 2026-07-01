from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.model import model
from app.schemas.embedding import EmbedRequest, EmbedResponse
from app.services.qdrant import ensure_collection_exists


@asynccontextmanager
async def lifespan(app: FastAPI):
    ensure_collection_exists()
    yield

app = FastAPI(
    title="Embedding Service",
    lifespan=lifespan,
    )


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "embedding",
        "model_loaded": model is not None,
    }
    
    
@app.post("/embed", response_model=EmbedResponse)
def embed(request: EmbedRequest):
    embedding = model.encode(request.text).tolist()
    
    return EmbedResponse(
        dimension=len(embedding),
        embedding=embedding,
    )