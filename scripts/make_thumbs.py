"""Generate tiny thumbnails for the Mochi grid tiles.

The grid tiles display at ~133px on screen, so a 320px thumb is plenty
and lets the entire grid load near-instantly on mobile while the full-res
PNGs (used for canvas compositing) stream in afterward.
"""

from PIL import Image
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "mochi"
DST = SRC / "thumb"
THUMB_DIM = 320

DST.mkdir(parents=True, exist_ok=True)


def process(src: Path) -> tuple[int, int]:
    img = Image.open(src)
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    w, h = img.size
    m = max(w, h)
    if m > THUMB_DIM:
        s = THUMB_DIM / m
        img = img.resize((max(1, round(w * s)), max(1, round(h * s))), Image.LANCZOS)
    out = DST / src.name
    img.save(out, "PNG", optimize=True)
    return src.stat().st_size, out.stat().st_size


def main() -> None:
    files = sorted(SRC.glob("*.png"), key=lambda p: int(p.stem) if p.stem.isdigit() else 999)
    total_thumb = 0
    for f in files:
        _orig, thumb = process(f)
        total_thumb += thumb
        print(f"  thumb/{f.name}: {thumb/1024:>4.0f}KB")
    print(f"\n  TOTAL THUMBS: {total_thumb/1024:.0f}KB across {len(files)} files")


if __name__ == "__main__":
    main()
