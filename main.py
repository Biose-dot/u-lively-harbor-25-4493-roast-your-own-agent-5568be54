#!/usr/bin/env python3
"""Copy the committed entry text to the output directory.

The entry lives in entry.txt next to this file; this script only copies
it to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Standard library only.
"""
import os

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(ASSET, "rb") as src:
        data = src.read()
    if not data.strip():
        raise ValueError("entry.txt is empty")
    with open(os.path.join(out_dir, "entry.txt"), "wb") as dst:
        dst.write(data)


if __name__ == "__main__":
    main()
