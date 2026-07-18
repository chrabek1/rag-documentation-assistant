from pathlib import Path

import pytest

from backend.app.loaders.txt_loader import load_txt


def test_load_txt_returns_file_content(tmp_path: Path):
    file_path = tmp_path / "sample.txt"
    expected_text = "Hello World\nThis is a test file."
    
    file_path.write_text(expected_text, encoding="utf-8")
    
    result = load_txt(file_path)
    
    assert result == expected_text

def test_load_txt_raises_file_not_found_error(tmp_path: Path):
    missing_file = tmp_path / "missing.txt"
    
    with pytest.raises(FileNotFoundError):
        load_txt(missing_file)