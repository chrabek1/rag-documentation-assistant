from pathlib import Path

from app.loaders.txt_loader import load_txt
from app.chunking.factory import ChunkerFactory
from app.services.qdrant import QdrantService
from app.services.embedding_client import EmbeddingClient


class IndexingService:
    def __init__(self, embedding_client: EmbeddingClient, qdrant_service: QdrantService):
        self.embedding_client = embedding_client
        self.qdrant_service = qdrant_service

    def index_document(
        self,
        path: Path,
        strategy: str,
        chunk_size: int,
        overlap: int,
    ) -> None:
        text = load_txt(path)

        chunker = ChunkerFactory.create(
            strategy=strategy,
            chunk_size=chunk_size,
            overlap=overlap,
        )

        chunks = chunker.chunk(text, path.name)
        embedded_chunks = self.embedding_client.embed(chunks)
        self.qdrant_service.index_chunks(embedded_chunks)