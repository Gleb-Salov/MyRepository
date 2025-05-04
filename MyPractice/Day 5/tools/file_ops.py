from pathlib import Path

def save_text_to_file(text, filename = "data/input.txt"):
    path = Path(filename)
    path.parent.mkdir(exist_ok=True)
    path.write_text(text, encoding="utf-8")

def read_text_from_file(filename="data/input.txt"):
    path = Path(filename)
    return path.read_text(encoding="utf-8")