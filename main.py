#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single warning-label line to entry.txt.
Pure standard library.
"""

import os

LINE = "WARNING: If you can read this label, you have already voided the warranty. It expired yesterday. And tomorrow."


def main():
    # A warning label is one line: fail loudly if that ever stops being true.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, "entry must fit the one-line limit"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
