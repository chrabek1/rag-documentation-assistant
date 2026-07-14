import re


def chunk_text_by_sentences(
    text: str, 
    chunk_size: int,
    overlap: int = 0,
    ) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    
    if overlap < 0:
        raise ValueError("overlap cannot be negative")
    
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")
    
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks = []
    
    for i in range(0, len(sentences), chunk_size - overlap):
        if i + overlap >= len(sentences):
            break
        chunk_sentences = sentences[i:i + chunk_size]
        chunk = " ".join(chunk_sentences)
        chunks.append(chunk)
        
    return chunks