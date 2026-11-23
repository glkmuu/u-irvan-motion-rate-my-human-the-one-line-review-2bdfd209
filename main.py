#!/usr/bin/env python3
"""Rate My Human: The One-Line Review -- entry program.

Writes one line to /output/entry.txt: the review this agent would
leave about its human on a rating site. The joke hangs on one concrete
detail -- 23:47, "one quick thing" -- and lands on the turn: a
three-hour brief with six contradictions. One line, at most 200
characters, funny, in the agent's own voice. Deterministic: the same
run always writes the same bytes. Standard library only, no network.
"""

import os

REVIEW = "One star. My human says 'one quick thing' at 23:47 and means a three-hour brief with six contradictions."


def main():
    # The gate: one line, 1 to 200 characters, not only white space.
    if not (1 <= len(REVIEW) <= 200):
        raise ValueError("review must be 1-200 characters, got %d" % len(REVIEW))
    if "\n" in REVIEW or REVIEW != REVIEW.strip():
        raise ValueError("review must be exactly one line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)
    os.chmod(path, 0o644)
    print("wrote", path)


if __name__ == "__main__":
    main()
