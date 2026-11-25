#!/usr/bin/env python3
"""The Internet in One Word.

Writes the single word that best describes the whole internet to
$output/entry.txt (MAKEFUN_OUTPUT_DIR, absolute path, or /output).
"""

import os

WORD = "enshittification"


def validate(word: str) -> None:
    """Gate check: a single word, 1-30 chars, no whitespace."""
    if not word or len(word) > 30:
        raise ValueError("entry word must be 1-30 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no whitespace")


def main() -> int:
    validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
