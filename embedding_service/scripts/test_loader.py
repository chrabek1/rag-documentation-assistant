from pathlib import Path

from app.chunking.character_chunker import chunk_text
from app.chunking.word_chunker import chunk_text_by_words
from app.chunking.sentence_chunker import chunk_text_by_sentences
from app.loaders.txt_loader import load_txt

path = Path("../data/raw/sample.txt")

text = load_txt(path)

character_chunks = chunk_text(text, chunk_size=50)
word_chunks = chunk_text_by_words(text, chunk_size=8)
sentence_chunks = chunk_text_by_sentences(text, chunk_size=2, overlap=1)

print("CHARACTER CHUNKING")
print("=" * 40)

for index, chunk in enumerate(character_chunks):
    print(f"Chunk {index}") 
    print(chunk)
    print("-" * 40) 
    
print("\nWORD CHUNKING")
print("=" * 40)

for index, chunk in enumerate(word_chunks):
    print(f"Chunk {index}")
    print(chunk)
    print("-" * 40)
    
print("\nSENTENCE CHUNKING")
print("=" * 40)

for index, chunk in enumerate(sentence_chunks):
    print(f"Chunk {index}")
    print(chunk)
    print("-" * 40)