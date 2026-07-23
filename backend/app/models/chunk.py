from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Chunk:
    text: str
    index: int
    document: str
    section: str | None = None
    
    def __post_init__(self) -> None:
        if not self.text.strip():
            raise ValueError("Chunk text cannot be empty.")
        if self.index < 0:
            raise ValueError("Chunk index cannot be negative.")
        if not self.document.strip():
            raise ValueError("Document name cannot be empty.")