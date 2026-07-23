from abc import ABC, abstractmethod

from app.models.chunk import Chunk


class BaseChunker(ABC):
    def __init__(self, chunk_size: int | None = None, overlap: int = 0):
        if chunk_size is not None:
            if chunk_size <= 0:
                raise ValueError("chunk_size must be greater than 0")
            
            if overlap < 0:
                raise ValueError("overlap cannot be negative")
            
            if overlap >= chunk_size:
                raise ValueError("overlap must be smaller than chunk_size")
            
        self.chunk_size = chunk_size
        self.overlap = overlap
        
    @abstractmethod
    def chunk(self, text: str, document: str) -> list[Chunk]:
        """Split text into chunks."""