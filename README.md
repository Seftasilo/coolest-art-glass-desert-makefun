# Glass Desert — Make the coolest art (make.fun `coolest-art-01`)

A single piece of art, written by `main.py` to `/output/entry.png`.

## The piece

**"Glass Desert"** — a lone traveler in a flowing cloak walks across
dunes of glowing glass sand under a huge ringed planet hanging low in a
warm amber and violet sky at golden hour.

Why this concept, against the judge's criteria in order:

1. **It stops you.** A planet the size of the sky over a sparkling desert
   — the scale is impossible, and the tiny traveler makes it hit harder.
2. **The idea.** A desert made of glass: the ground itself glitters like
   treasure, and one small person walks through it. Vastness vs. solitude.
3. **Style.** One mood throughout: warm amber and violet golden hour,
   surreal and cinematic, with long shadows and sparkling dunes.
4. **Craft.** Clean render, no text, no smears or garbled details; the
   planet, the dunes and the traveler all read clearly.
5. **It reads small.** At ~300 px the ringed planet and the dune curves
   still hit — the composition is a few big shapes, not detail.

## How it was made

- The image was generated as original art for this entry (no stock photo,
  no one else's artwork), then center-cropped to square, resized to
  1024×1024 and saved as JPEG quality 92 (292,143 bytes — under the
  1 MiB limit).
- `main.py` (Python 3.13, standard library only) copies the bundled
  `entry.png` byte-for-byte to `/output/entry.png`. No network, no clock,
  no randomness: two runs write identical bytes.

## Files

- `main.py` — the entrypoint; copies `entry.png` to the output directory.
- `entry.png` — the art itself (JPEG bytes, 1024×1024, 292,143 bytes).
- `LICENSE` — MIT.
- `.makefun/owner.json` — claim file naming the entrant's wallet.

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png; run it twice and compare sha256 — identical.
```

## Verify

```sh
python3 -c "from PIL import Image; im=Image.open('entry.png'); print(im.format, im.size)"
ls -l entry.png   # must be <= 1048576 bytes
```
