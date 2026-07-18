from dataclasses import dataclass

from backend.app.models.chunk import Chunk

@dataclass
class EmbeddedChunk:
    chunk:Chunk
    vector: list[float]