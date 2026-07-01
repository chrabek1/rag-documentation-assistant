from pydantic import BaseModel

class EmbedRequest(BaseModel):
    text: str
    
class EmbedResponse(BaseModel):
    dimension: int
    embedding: list[float]
    
class IndexTextRequest(BaseModel):
    text: str
    source: str = "manual"
    section: str = "unknown"
    chunk: int = 0
    
class IndexTextResponse(BaseModel):
    id: str
    status: str
    