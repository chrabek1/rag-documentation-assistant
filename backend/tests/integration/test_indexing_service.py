from pathlib import Path

from backend.app.services.indexing import IndexingService
from backend.app.models.chunk import Chunk


def test_index_document_returns_chunks(tmp_path: Path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text(
        "Sentence one. Sentence two. Sentence three.",
        encoding="utf-8",
    )
    
    service = IndexingService()
    
    chunks = service.index_document(
        path=file_path,
        strategy="sentence",
        chunk_size=2,
        overlap=1,
    )
    
    assert len(chunks) > 0
    assert chunks[0].index == 0
    assert isinstance(chunks[0], Chunk)
    assert isinstance(chunks[0].text, str)