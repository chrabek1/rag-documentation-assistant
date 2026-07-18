from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from uuid import uuid4


from app.core.config import settings
from app.model import model

client = QdrantClient(
    host=settings.qdrant_host,
    port=settings.qdrant_port,
)


def ensure_collection_exists() -> None:
    collection_names = [
        collection.name
        for collection in client.get_collections().collections
    ]
    
    if settings.collection_name in collection_names:
        return
    
    vector_size = model.get_sentence_embedding_dimension()
    
    client.create_collection(
        collection_name=settings.collection_name,
        vectors_config=VectorParams(
            size=vector_size,
            distance=Distance.COSINE,
        ),
    )
    
def index_text(
    text: str,
    vector: list[float],
    source: str,
    section: str,
    chunk: int,
) -> str:
    point_id = str(uuid4())
    
    client.upsert(
        collection_name=settings.collection_name,
        points=[
            PointStruct(
                id=point_id,
                vector=vector,
                payload={
                    "text": text,
                    "source": source,
                    "section": section,
                    "chunk": chunk,
                },
            )
        ],
    )
    
    return point_id