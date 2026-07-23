from app.chunking.base.base_chunker import BaseChunker
from app.models.chunk import Chunk


class TokenChunker(BaseChunker):
    def __init__(
        self,
        tokenizer,
        chunk_size: int,
        overlap: int = 0,
    ):
        self.tokenizer = tokenizer
        super().__init__(chunk_size,overlap)
        
    def chunk(self, text: str, document: str) -> list[Chunk]:
        token_ids = self.tokenizer.encode(text, add_special_tokens=False)
        chunks = []
        step = self.chunk_size - self.overlap

        for chunk_index, i in enumerate(range(0, len(token_ids), step)):
            if i + self.overlap >= len(token_ids):
                break
            chunk_token_ids = token_ids[i:i + self.chunk_size]
            chunk = self.tokenizer.decode(
                chunk_token_ids,
                skip_special_tokens=True,
            )
            chunks.append(
                Chunk(
                    text=chunk,
                    index=chunk_index,
                    document=document,
                )
            )
            
        return chunks