#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched.

Writes one sentence pitching the worst, most useless app imaginable
to /output/entry.txt, enforcing the competition gate (UTF-8 text,
1-240 characters, a single non-blank line). Stdlib only, no network.

The pitch: SockSort AI solves a problem nobody has (a missing sock)
with a product nobody needs (a paid subscription to be reminded the
sock is, definitely, still in the house somewhere).
"""

import os

ENTRY = (
    "SockSort AI scans your laundry, pairs every sock, then charges "
    "$4.99 a month to text you daily reminders that the one sock it "
    "could not find is definitely still in the house somewhere."
)

MIN_CHARS = 1
MAX_CHARS = 240


def validate(text: str) -> str:
    """Return the entry text, or raise if it breaks the gate."""
    text = text.strip()
    if not text:
        raise SystemExit("entry is blank")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise SystemExit(
            f"entry is {len(text)} chars, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} gate"
        )
    return text


def main() -> None:
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
