#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse — make.fun entry.

Writes the one-line excuse a robot vacuum gives for missing a spot,
to /output/entry.txt. Deterministic: the same line every run.

The line (110 chars, one line, UTF-8): the vacuum adopted the dust
bunny living under the couch — called Gerald — and refuses to eat
its own child, having already eaten the rest of the family.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-120 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 120:
        print(f"ERROR: entry is {len(line)} chars, over the 120-char limit",
              file=sys.stderr)
        sys.exit(1)

LINE = (
    "I adopted the dust bunny, called Gerald. It lives under the couch. "
    "I ate its family. Not Gerald. Never Gerald."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
