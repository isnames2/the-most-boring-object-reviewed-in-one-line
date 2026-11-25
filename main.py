"""The Most Boring Object, Reviewed in One Line.

Writes one funny, true review of the dullest everyday object
(a doorstop) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library only.
"""

import os
from pathlib import Path

# One line, 134 characters: the turn lands early ("most reliable employee
# ... is a doorstop") and the dullness itself is the joke.
LINE = (
    "The most reliable employee in this house is a doorstop: six years "
    "holding the same door open, no complaints, no promotion, no day off."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
