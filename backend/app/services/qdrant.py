from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from uuid import uuid4


from app.core.config import settings
from app.models.embedded_chunk import EmbeddedChunk

class QdrantService:
    def __init__(self):
        self.client = QdrantClient(
            host=settings.qdrant_host,
            port=settings.qdrant_port,
        )


    def ensure_collection_exists(self, vector_size: int) -> None:
        collection_names = [
            collection.name
            for collection in self.client.get_collections().collections
        ]
        
        if settings.collection_name in collection_names:
            return
        
        self.client.create_collection(
            collection_name=settings.collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )
        
    def index_chunks(
        self,
        embedded_chunks: list[EmbeddedChunk],
    ) -> None:
        if not embedded_chunks:
            return
        
        self.ensure_collection_exists(
            vector_size=len(embedded_chunks[0].vector)
        )
        
        self.client.upsert(
            collection_name=settings.collection_name,
            points=[
                PointStruct(
                    id=str(uuid4()),
                    vector=embedded_chunk.vector,
                    payload={
                        "text": embedded_chunk.chunk.text,
                        "chunk_index": embedded_chunk.chunk.index,
                        "section": embedded_chunk.chunk.section,
                        "document": embedded_chunk.chunk.document,
                        
                    },
                )
                for embedded_chunk in embedded_chunks
            ],
        )