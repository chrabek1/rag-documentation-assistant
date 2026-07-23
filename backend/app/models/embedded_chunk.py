from dataclasses import dataclass

from app.models.chunk import Chunk

@dataclass
class EmbeddedChunk:
    chunk:Chunk
    vector: list[float]