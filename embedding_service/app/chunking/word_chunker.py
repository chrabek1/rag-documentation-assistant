from app.chunking.base.base_chunker import BaseChunker


class WordChunker(BaseChunker):
    def __init__(self, chunk_size: int):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")
        
        self.chunk_size = chunk_size
        
    def chunk(self, text: str) -> list[str]:
        words = text.split()
        chunks = []
        
        for i in range(0, len(words), self.chunk_size):
            chunk_words = words[i:i + self.chunk_size]
            chunks.append(" ".join(chunk_words))
            
        return chunks