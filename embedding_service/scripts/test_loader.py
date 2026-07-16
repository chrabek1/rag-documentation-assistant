from pathlib import Path


from app.chunking.factory import ChunkerFactory
from app.loaders.txt_loader import load_txt

from app.model import model

path = Path("/data/raw/sample.txt")

text = load_txt(path)

character_chunker = ChunkerFactory.create(strategy="character", chunk_size=50)
word_chunker = ChunkerFactory.create(strategy="word", chunk_size=8)
sentence_chunker = ChunkerFactory.create(strategy="sentence", chunk_size=2, overlap=1)
paragraph_chunker = ChunkerFactory.create(strategy="paragraph")
token_chunker = ChunkerFactory.create(strategy="token", tokenizer=model.tokenizer, chunk_size=10)

character_chunks = character_chunker.chunk(text)
word_chunks = word_chunker.chunk(text)
sentence_chunks = sentence_chunker.chunk(text)
paragraph_chunks = paragraph_chunker.chunk(text)
token_chunks = token_chunker.chunk(text)

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
    
print("\nPARAGRAPH CHUNKING")
print("=" * 40)

for index, chunk in enumerate(paragraph_chunks):
    print(f"Chunk {index}")
    print(chunk)
    print("-" * 40)
    
print("\nTOKEN CHUNKING")
print("=" * 40)

for index, chunk in enumerate(token_chunks):
    print(f"Chunk {index}")
    print(chunk)
    print("-" * 40)