import re

from app.chunking.base.base_chunker import BaseChunker
from app.models.chunk import Chunk


class SentenceChunker(BaseChunker):
    
    def __init__(self, chunk_size: int, overlap: int = 0):
        super().__init__(chunk_size, overlap)

    def chunk(self, text: str, document: str) -> list[Chunk]:
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
                    document=document,
                    )
                )
            
        return chunks