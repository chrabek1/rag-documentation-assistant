import re

from backend.app.chunking.base.base_chunker import BaseChunker
from app.models.chunk import Chunk
class ParagraphChunker(BaseChunker):
    def chunk(self, text: str) -> list[Chunk]:
        paragraphs = re.split(r"\n\s*\n", text)
        
        return [
            Chunk(
                text = paragraph.strip(),
                index = index
            )
            for index, paragraph in enumerate(paragraphs)
            if paragraph.strip()
        ]