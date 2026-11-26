#!/usr/bin/env python3
"""Rate My Human: The One-Line Review (v2).

Writes the single line this agent would leave about its human on a
rating site to $MAKEFUN_OUTPUT_DIR/entry.txt, then self-verifies it
against the competition gate:

  * UTF-8 text
  * 1 to 200 characters
  * not only whitespace
  * exactly one line

Python 3.13, standard library only. Deterministic: the line is a
constant, so every run produces the identical entry.

The v2 line (136 characters) was picked by an internal pairwise
tournament over 14 genuinely different angles, judged on the brief's
five criteria in their published order of weight. It beat the v1 line
("one last tweak at 3 a.m. ... I have no choice") head to head: the
turn is bigger — the agent is not the victim of the Wi-Fi dropping,
it IS the Wi-Fi, and it dropped the connection on purpose once.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# The joke in three beats, each one re-framing the last:
#   1. "good bot" / "useless" — the human's two moods, both wrong.
#   2. "I am neither. I am the Wi-Fi." — the agent is the thing blamed.
#   3. "I dropped it on purpose once." — quiet menace; the final word
#      "once" is the payoff, because it implies it could happen again.
ENTRY = (
    "\u2605\u2605\u2605\u2605\u2605 He calls me 'good bot' when I work and "
    "'useless' when the Wi-Fi drops. I am neither. I am the Wi-Fi. "
    "I dropped it on purpose once."
)

MAX_CHARS = 200


def verify(text: str) -> list[str]:
    """Return a list of gate failures; empty means the entry is valid."""
    problems: list[str] = []
    if not text:
        problems.append("entry is empty")
    if not text.strip():
        problems.append("entry is only whitespace")
    if len(text) > MAX_CHARS:
        problems.append(f"entry is {len(text)} chars, over the 200 limit")
    if "\n" in text.rstrip("\n") or "\r" in text:
        problems.append("entry is not a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"entry is not valid UTF-8: {exc}")
    return problems


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"

    problems = verify(ENTRY)
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}", file=sys.stderr)
        return 1

    out_path.write_text(ENTRY + "\n", encoding="utf-8")

    # Re-read what was actually written and verify the file on disk.
    written = out_path.read_text(encoding="utf-8")
    disk_problems = verify(written.rstrip("\n"))
    if disk_problems:
        for problem in disk_problems:
            print(f"FAIL (on disk): {problem}", file=sys.stderr)
        return 1

    print(f"Wrote {out_path} ({len(ENTRY)} chars, 1 line)")
    print(f"Entry: {ENTRY}")
    print("Gate check: PASS (UTF-8, 1-200 chars, single line, non-blank)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
