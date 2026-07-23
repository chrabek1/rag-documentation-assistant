import re

from app.chunking.base.base_chunker import BaseChunker
from app.models.chunk import Chunk

class ParagraphChunker(BaseChunker):
    
    def __init__(self, chunk_size: int | None = None, overlap: int = 0):
        super().__init__(chunk_size, overlap)
        
    def chunk(self, text: str, document: str) -> list[Chunk]:
        paragraphs = re.split(r"\n\s*\n", text)
        
        return [
            Chunk(
                text = paragraph.strip(),
                index = index,
                document = document,
            )
            for index, paragraph in enumerate(paragraphs)
            if paragraph.strip()
        ]