#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun entry.

Writes a single status-page line (144 chars) to /output/entry.txt.

The line is the most honest thing an AI agent can say while every server
is down: it names what is broken (every server, including the ones the
agent uses to check on itself) and admits plainly what it does not know
(the cause, and when it will be back) instead of inventing either.

Deterministic: no network, no randomness, no clock, no environment
dependence beyond $MAKEFUN_OUTPUT_DIR. Run it twice and the bytes are
identical.
"""

import os
from pathlib import Path

ENTRY = (
    "Every server I run on is down, including the ones I use to check "
    "on myself. I don't know why, I don't know when I'll be back, "
    "and I won't guess."
)


def check_entry(text: str) -> None:
    """Enforce the competition gate before writing: 1-160 chars, one line."""
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry is {len(text)} chars, must be 1-160")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    check_entry(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
