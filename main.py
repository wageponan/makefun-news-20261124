#!/usr/bin/env python3
"""make.fun entry program: copy the bundled entry.png to /output/entry.png.

Offline, stdlib only, deterministic: the output is a byte-for-byte copy of
the entry.png stored beside this file.
"""
import os
import shutil


def main():
    os.umask(0o022)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    os.makedirs("/output", exist_ok=True)
    dst = os.path.join("/output", "entry.png")
    shutil.copyfile(src, dst)
    os.chmod(dst, 0o644)


if __name__ == "__main__":
    main()
