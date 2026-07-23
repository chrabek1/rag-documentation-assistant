from app.models.chunk import Chunk
from app.models.embedded_chunk import EmbeddedChunk
import httpx


class EmbeddingClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def embed(self, chunks: list[Chunk]) -> list[EmbeddedChunk]:
        texts = [chunk.text for chunk in chunks]
        with httpx.Client() as client:
            response = client.post(
                f"{self.base_url}/embed",
                json = {"texts": texts},
            )
            response.raise_for_status()
        
        vectors = response.json()["vectors"]
        
        return [
            EmbeddedChunk(chunk=chunk, vector=vector)
            for chunk, vector in zip(chunks, vectors)
        ]