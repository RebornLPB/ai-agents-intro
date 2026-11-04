import re

required_sections = [
    "Topic",
    "Simple Explanation",
    "Key Concepts",
    "Example",
    "Practice Exercise",
    "Common Mistakes",
    "Review Comments",
    "Final Summary",
]

def validate_required_sections(markdown: str) -> dict:
    headings = []
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("#"):
            headings.append(line.lstrip("#").strip().lower())

    missing = []
    for section in required_sections:
        if section.lower() not in headings:
            missing.append(section)

    return {"is_valid": len(missing) == 0, "missing_sections": missing}
