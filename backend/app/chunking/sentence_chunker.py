import re

from backend.app.chunking.base.base_chunker import BaseChunker
from app.models.chunk import Chunk

class SentenceChunker(BaseChunker):
    def __init__(self, chunk_size: int, overlap: int = 0):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")
        
        if overlap < 0:
            raise ValueError("overlap cannot be negative")
        
        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")
        
        self.chunk_size = chunk_size
        self.overlap = overlap


    def chunk(self, text: str) -> list[Chunk]:
        sentences = re.split(r"(?<=[.!?])\s+", text)
        chunks = []
        step = self.chunk_size - self.overlap
        for i in range(0, len(sentences), step):
            if i + self.overlap >= len(sentences):
                break
            chunk_sentences = sentences[i:i + self.chunk_size]
            chunks.append(
                Chunk(
                    text=" ".join(chunk_sentences),
                    index=len(chunks),
                    )
                )
            
        return chunks