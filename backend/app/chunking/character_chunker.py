from app.chunking.base.base_chunker import BaseChunker
from app.models.chunk import Chunk


class CharacterChunker(BaseChunker):

    def __init__(self, chunk_size: int, overlap: int = 0):
        super().__init__(chunk_size, overlap)
    
    def chunk(self, text: str, document: str) -> list[Chunk]:
        
        chunks = []
        
        for i in range(0, len(text), self.chunk_size):
            chunks.append(
                Chunk(
                    text=text[i:i + self.chunk_size],
                    index=len(chunks),
                    document=document,
                )
            )
            
        return chunks