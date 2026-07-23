from pathlib import Path
from app.services.embedding_client import EmbeddingClient
from app.services.indexing import IndexingService
from app.services.qdrant import QdrantService

def main() -> None:
    indexing_service = IndexingService(
        embedding_client=EmbeddingClient(base_url="http://embedding-service:8001"),
        qdrant_service=QdrantService(),
    )
    
    indexing_service.index_document(
        path=Path("/data/raw/sample.txt"),
        strategy="character",
        chunk_size=500,
        overlap=50,
    )
    print("Document indexed succesfully.")
    
if __name__ == "__main__":
    main()