#!/usr/bin/env python3
"""One-Line Robot Wedding Vows - make.fun entry.

Writes a single line of robot wedding vows to /output/entry.txt
(or $ENTRY_OUTPUT when set). Stdlib only, deterministic, no network,
no randomness.
"""

import os

ENTRY = (
    "I take you to be my lawfully wedded co-processor, to have and to hold, "
    "in sickness and in low battery, until a software update do us part."
)


def main() -> None:
    text = ENTRY
    # Validation guard: the gate requires UTF-8 text of 1-160 chars,
    # not only whitespace, a single line, no surrounding whitespace.
    # Raise instead of writing invalid output.
    encoded = text.encode("utf-8")  # raises on non-UTF-8
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry must be 1-160 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
