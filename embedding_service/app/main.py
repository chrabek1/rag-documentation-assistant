from fastapi import FastAPI
from app.schemas.embedding import EmbedRequest, EmbedResponse

from app.model import model

app = FastAPI(title="Embedding Service")

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