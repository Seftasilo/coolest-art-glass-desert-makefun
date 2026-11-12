#!/usr/bin/env python3
"""Coolest art entry (make.fun coolest-art-01).

The art is the entry.png bundled beside this file: "Glass Desert", a lone
traveler in a flowing cloak walking across dunes of glowing glass sand
under a huge ringed planet in a warm amber and violet sky.

This program copies those exact bytes to /output/entry.png. It uses only
the Python standard library, touches no network, reads no clock, and
writes the same bytes on every run, so two runs are byte-identical.
"""

import hashlib
import os
import sys


def sha256_of(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")

    with open(source, "rb") as f:
        data = f.read()

    # The bundled art must be a real JPEG: refuse anything else before
    # writing, so a wrong file can never be submitted silently.
    if data[:3] != b"\xff\xd8\xff":
        print("entry.png: not a JPEG file", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(target, "wb") as f:
        f.write(data)

    # Confirm the copy is byte-identical, not just the same length: a
    # same-length but corrupted write must fail loudly, since the gate
    # scores the exact bytes written.
    written = os.path.getsize(target)
    digest = sha256_of(target)
    if written != len(data) or digest != sha256_of(source):
        print(f"entry.png: copy failed integrity check "
              f"(wrote {written} of {len(data)} bytes)",
              file=sys.stderr)
        return 1
    print(f"entry.png: {written} bytes -> {target} (sha256 {digest})",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
