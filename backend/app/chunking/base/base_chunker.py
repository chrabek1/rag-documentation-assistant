from abc import ABC, abstractmethod

from app.models.chunk import Chunk

class BaseChunker(ABC):
    
    @abstractmethod
    def chunk(self, text: str) -> list[Chunk]:
        pass