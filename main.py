#!/usr/bin/env python3
"""Write one sentence explaining the modern internet to a traveler from 1800.

The sentence is fixed text: no randomness, no network, no clock, so two
runs always produce byte-identical output. Every word in it predates 1800
(a road, a post office, a library, a market square), so a traveler from
that year can picture it; the road reaching the front door is the one
image that carries what the internet does.
"""

import os

SENTENCE = (
    "Think of one road joining every post office, library, and market "
    "square on earth to your front door, so you can send a letter, read "
    "a book, or speak with anyone in a breath."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
