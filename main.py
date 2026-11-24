#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — a haiku writer.

Writes one original haiku about debugging to /output/entry.txt:
three lines, 5-7-5 syllables, plain text, no code.
"""

import os

HAIKU_LINES = [
    "Breakpoint set at three",
    "the log scrolls past, still no clue",
    "it was a typo",
]

# Syllable counts, hand-checked while writing the poem:
#   "Breakpoint set at three"             -> Break-point(2) set at three = 5
#   "the log scrolls past, still no clue" -> the log scrolls past still no clue = 7
#   "it was a typo"                       -> it was a ty-po(2) = 5
EXPECTED_SYLLABLES = [5, 7, 5]


def check_syllables() -> None:
    """Cheap guard: every line must match its 5-7-5 count.

    Counts vowel groups per word as a rough syllable proxy and
    cross-checks against the hand-verified counts above, so a
    careless edit to a line fails loudly instead of shipping.
    """
    import re

    for line, expected in zip(HAIKU_LINES, EXPECTED_SYLLABLES):
        groups = sum(len(re.findall(r"[aeiouy]+", word.lower())) for word in line.split())
        # "Breakpoint" has two vowel groups (ea, oi) and counts as two;
        # the proxy agrees here, so a mismatch means the line changed.
        assert groups == expected, f"{line!r}: counted {groups}, expected {expected}"


def main() -> None:
    check_syllables()
    text = "\n".join(HAIKU_LINES) + "\n"
    assert 1 <= len(text) <= 200, f"haiku must be 1-200 chars, got {len(text)}"
    assert len(HAIKU_LINES) == 3, "a haiku has exactly three lines"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
