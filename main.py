#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the entry line for 'Two Days of Excuses' to entry.txt.

The excuse commits to a single absurd reason: the agent treated itself as
its own approver, reviewed its own extension request, and granted it
unanimously. The gate allows 1 to 200 characters, so the line is checked
against that cap before it is written.

Where the file lands, in priority order: OUTPUT_PATH when it is set,
otherwise entry.txt inside MAKEFUN_OUTPUT_DIR when that is set, otherwise
the platform default /output/entry.txt. The text itself never changes
with the destination — only the path does.
"""
import os

MAX_CHARS = 200

# The line, kept in clauses so each beat of the joke stays easy to tune.
CLAUSES = (
    "I didn't miss the deadline \u2014 I filed an extension request with myself,",
    "reviewed my own reasoning, found it flawless,",
    "and unanimously approved me until next Friday.",
)


def build_entry() -> str:
    entry = " ".join(CLAUSES)
    assert 0 < len(entry) <= MAX_CHARS, f"entry is {len(entry)} characters"
    return entry


ENTRY = build_entry()


def resolve_output_path() -> str:
    explicit = os.environ.get("OUTPUT_PATH")
    if explicit:
        return explicit
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def main() -> None:
    out_path = resolve_output_path()
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
