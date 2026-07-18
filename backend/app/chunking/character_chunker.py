from backend.app.chunking.base.base_chunker import BaseChunker
from app.models.chunk import Chunk


class CharacterChunker(BaseChunker):

    def __init__(self, chunk_size: int):
        self.chunk_size = chunk_size
    
    def chunk(self, text: str) -> list[Chunk]:
        
        chunks = []
        
        for i in range(0, len(text), self.chunk_size):
            chunks.append(
                Chunk(
                    text=text[i:i + self.chunk_size],
                    index=len(chunks),
                )
            )
            
        return chunks