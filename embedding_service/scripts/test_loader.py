from pathlib import Path

from app.chunking.character_chunker import CharacterChunker
from app.chunking.word_chunker import WordChunker
from app.chunking.sentence_chunker import SentenceChunker
from app.chunking.paragraph_chunker import ParagraphChunker
from app.chunking.token_chunker import TokenChunker
from app.loaders.txt_loader import load_txt

from app.model import model

path = Path("/data/raw/sample.txt")

text = load_txt(path)

character_chunker = CharacterChunker(chunk_size=50)
word_chunker = WordChunker(chunk_size=8)
sentence_chunker = SentenceChunker(chunk_size=2, overlap=1)
paragraph_chunker = ParagraphChunker()
token_chunker = TokenChunker(tokenizer=model.tokenizer, chunk_size=10)

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