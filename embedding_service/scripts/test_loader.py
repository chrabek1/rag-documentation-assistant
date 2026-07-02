from pathlib import Path

from app.chunking.simple_chunker import chunk_text
from app.loaders.txt_loader import load_txt

path = Path("../data/raw/sample.txt")

text = load_txt(path)

chunks = chunk_text(text, chunk_size=50)

for index, chunk in enumerate(chunks):
    print(f"Chunk {index}")
    print(chunk)
    print("-" * 40)