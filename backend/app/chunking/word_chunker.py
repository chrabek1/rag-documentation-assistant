from backend.app.chunking.base.base_chunker import BaseChunker
from app.models.chunk import Chunk


class WordChunker(BaseChunker):
    def __init__(self, chunk_size: int):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")
        
        self.chunk_size = chunk_size
        
    def chunk(self, text: str) -> list[Chunk]:
        words = text.split()
        chunks = []
        
        for chunk_index, i in enumerate(range(0, len(words), self.chunk_size)):
            chunk_words = words[i:i + self.chunk_size]
            chunks.append(
                Chunk(
                    text=" ".join(chunk_words),
                    index=chunk_index,
                )
                )
            
        return chunks