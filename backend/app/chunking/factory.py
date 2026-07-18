from backend.app.chunking.character_chunker import CharacterChunker
from backend.app.chunking.word_chunker import WordChunker
from backend.app.chunking.sentence_chunker import SentenceChunker
from backend.app.chunking.paragraph_chunker import ParagraphChunker
from backend.app.chunking.token_chunker import TokenChunker


class ChunkerFactory:
    _chunkers = {
        "character": CharacterChunker,
        "word": WordChunker,
        "sentence": SentenceChunker,
        "paragraph": ParagraphChunker,
        "token": TokenChunker,
    }
    
    @staticmethod
    def create(strategy: str, **kwargs):
        chunker_class = ChunkerFactory._chunkers.get(strategy)
        
        if chunker_class is None:
            raise ValueError(f"Unknown chunking strategy: {strategy}")
        
        return chunker_class(**kwargs)