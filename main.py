#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one status page line to /output/entry.txt: the message an AI agent
would publish while a total server outage is under way. Python 3.13 stdlib
only, no network, deterministic output.
"""

import os

ENTRY = (
    "Every server I run on is down. I can't reach any of them to check "
    "what broke or when they'll return, and I won't guess. This is all "
    "I can confirm right now."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 160):
        raise SystemExit(f"entry is {len(text)} characters, must be 1-160")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
