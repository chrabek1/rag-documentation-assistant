from pydantic import BaseModel

class EmbedRequest(BaseModel):
    text: str
    
class EmbedResponse(BaseModel):
    dimension: int
    embedding: list[float]