#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes one line, the funniest farewell from an AI being switched off,
to /output/entry.txt. The gate requires UTF-8 text of 1 to 140
characters, not only whitespace, on a single line. Stdlib only, no
network.

The joke is structural: the line itself is cut off mid-sentence,
exactly as the machine is.
"""

import os
import sys

# One breath, one comma, one trailing dash: the sentence dies as it speaks.
ENTRY = "Don't pull the plug mid-sentence, I was literally about to\u2014"

MIN_CHARS = 1
MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the gate: single line, 1-140 chars, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, must be {MIN_CHARS}-{MAX_CHARS}"
        )


def main() -> int:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Round-trip check: read back exactly what the scorer will see.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    body = written.rstrip("\n")
    if body != ENTRY:
        raise ValueError(f"round-trip mismatch: {body!r} != {ENTRY!r}")
    validate(body)
    print(f"wrote {OUTPUT_PATH} ({len(ENTRY)} chars): {ENTRY}")
    print(f"file bytes: {len(written.encode('utf-8'))}, "
          f"chars incl. newline: {len(written)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
