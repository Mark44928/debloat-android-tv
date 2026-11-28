#!/data/data/com.termux/files/usr/bin/env python3
"""debloat-android-tv package list — print every package documented in the README.

Read-only. No root, no device. Extracts `com.*` / `org.*` package IDs from
README.md so you can see what the scripts cover.

Usage:
    python3 list.py            # list packages
    python3 list.py --count    # just the count
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
README = os.path.join(HERE, "README.md")
PKG_RE = re.compile(r"\b(?:com|org|net)\.[a-zA-Z0-9_.]+\b")


def main(argv):
    with open(README, encoding="utf-8") as fh:
        text = fh.read()
    pkgs = sorted(set(PKG_RE.findall(text)))
    if "--count" in argv:
        print(len(pkgs))
        return 0
    for p in pkgs:
        print(p)
    print(f"\n{len(pkgs)} packages documented", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))