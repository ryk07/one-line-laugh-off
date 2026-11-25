#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one original funny line to /output/entry.txt.
Stdlib only; paths resolved from this file, never from the cwd.
"""
import os

LINE = "My password manager forgot my password, so now we sit in silence staring at the login screen together."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %d chars to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
