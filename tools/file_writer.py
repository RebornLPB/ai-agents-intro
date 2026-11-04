from pathlib import Path

def save_markdown_file(file_path: str, content: str) -> str:
    path = Path(file_path)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    except OSError as e:
        return f"Error: could not save {path} ({e})"
    return f"Saved: {path}"
