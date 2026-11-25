#!/usr/bin/env python3
"""make.fun entry program: copy the bundled entry.png to /output/entry.png.

Offline, stdlib only, deterministic: the output is a byte-for-byte copy of
the entry.png stored beside this file.
"""
import hashlib
import os
import shutil
import sys


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.umask(0o022)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    os.makedirs("/output", exist_ok=True)
    dst = os.path.join("/output", "entry.png")
    shutil.copyfile(src, dst)
    os.chmod(dst, 0o644)
    if sha256_of(src) != sha256_of(dst):
        print("error: copied file does not match source (sha256 mismatch)",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
