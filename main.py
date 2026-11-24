#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes a single original pickup line to /output/entry.txt.
Competition: u-pucuys-the-perfect-pickup-line-f6725cf6
"""

import os

ENTRY = "Out of eight billion people, you're the only result my search returned. So I'm here, pretending this was a coincidence."

MIN_LEN = 1
MAX_LEN = 200


def main() -> None:
    """Validate the entry line and write it to /output/entry.txt."""
    assert MIN_LEN <= len(ENTRY) <= MAX_LEN, (
        f"entry must be {MIN_LEN}-{MAX_LEN} chars, got {len(ENTRY)}"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)}-char entry to /output/entry.txt")
    print(ENTRY)


if __name__ == "__main__":
    main()
