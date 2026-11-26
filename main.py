#!/usr/bin/env python3
"""One-star alien tourist review of Earth — with a genuine five-star verdict on the food.

Deterministic: no randomness, no time, no I/O beyond writing the entry.
Writes exactly one sentence to /output/entry.txt.
"""

import os

ENTRY = (
    "Earth's gravity flattened my knees, the queue outlasted my planet's "
    "entire orbit, and the rain fell sideways, yet the noodles were so "
    "good I would crash-land here again just to eat them."
)

# Guard: the entry must be exactly one sentence, 1-200 UTF-8 characters.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
