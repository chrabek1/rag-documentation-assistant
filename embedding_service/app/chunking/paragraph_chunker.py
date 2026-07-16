import re

from app.chunking.base.base_chunker import BaseChunker

class ParagraphChunker(BaseChunker):
    def chunk(self, text: str) -> list[str]:
        paragraphs = re.split(r"\n\s*\n", text)
        
        return [
            paragraph.strip()
            for paragraph in paragraphs
            if paragraph.strip()
        ]