from app.chunking.base.base_chunker import BaseChunker
from app.models.chunk import Chunk


class WordChunker(BaseChunker):
    def __init__(self, chunk_size: int, overlap: int = 0):
        super().__init__(chunk_size, overlap)
        
    def chunk(self, text: str, document: str) -> list[Chunk]:
        words = text.split()
        chunks = []
        step = self.chunk_size - self.overlap
        
        for chunk_index, i in enumerate(range(0, len(words), step)):
            chunk_words = words[i:i + self.chunk_size]
            chunks.append(
                Chunk(
                    text=" ".join(chunk_words),
                    index=chunk_index,
                    document=document,
                )
                )
            if i + self.overlap >= len(words):
                break

        return chunks