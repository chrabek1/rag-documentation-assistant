from app.chunking.base.base_chunker import BaseChunker


class CharacterChunker(BaseChunker):

    def __init__(self, chunk_size: int):
        self.chunk_size = chunk_size
    
    def chunk(self, text: str) -> list[str]:
        
        chunks = []
        
        for i in range(0, len(text), self.chunk_size):
            chunks.append(text[i:i + self.chunk_size])
            
        return chunks