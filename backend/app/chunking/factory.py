from app.chunking.character_chunker import CharacterChunker
from app.chunking.word_chunker import WordChunker
from app.chunking.sentence_chunker import SentenceChunker
from app.chunking.paragraph_chunker import ParagraphChunker
from app.chunking.token_chunker import TokenChunker
from app.chunking.base.base_chunker import BaseChunker


class ChunkerFactory:
    _chunkers = {
        "character": CharacterChunker,
        "word": WordChunker,
        "sentence": SentenceChunker,
        "paragraph": ParagraphChunker,
        "token": TokenChunker,
    }
    
    @staticmethod
    def create(strategy: str, **kwargs) -> BaseChunker:
        chunker_class = ChunkerFactory._chunkers.get(strategy)
        
        if chunker_class is None:
            raise ValueError(f"Unknown chunking strategy: {strategy}")
        
        return chunker_class(**kwargs)