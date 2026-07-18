from pathlib import Path

from backend.app.loaders.txt_loader import load_txt
from backend.app.chunking.factory import ChunkerFactory


class IndexingService:

    def index_document(
        self,
        path: Path,
        strategy: str,
        chunk_size: int,
        overlap: int,
    ):
        text = load_txt(path)

        chunker = ChunkerFactory.create(
            strategy=strategy,
            chunk_size=chunk_size,
            overlap=overlap,
        )

        chunks = chunker.chunk(text)

        return chunks