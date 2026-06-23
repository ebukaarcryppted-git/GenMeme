"""Resize each Mochi PNG down to a max dimension so mobile can fetch them fast.

The canvas overlay never needs more than ~768px wide at scale 1; capping
at 1024px keeps zoom up to ~3x sharp while cutting file size dramatically.
Aspect ratio and alpha channel are preserved.
"""

from PIL import Image
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "mochi"
MAX_DIM = 1024


def process(path: Path) -> None:
    img = Image.open(path)
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    w, h = img.size
    m = max(w, h)
    if m > MAX_DIM:
        s = MAX_DIM / m
        new_w = max(1, round(w * s))
        new_h = max(1, round(h * s))
        img = img.resize((new_w, new_h), Image.LANCZOS)
    img.save(path, "PNG", optimize=True)


def main() -> None:
    files = sorted(SRC.glob("*.png"), key=lambda p: int(p.stem) if p.stem.isdigit() else 999)
    total_before = 0
    total_after = 0
    for f in files:
        before = f.stat().st_size
        process(f)
        after = f.stat().st_size
        total_before += before
        total_after += after
        print(f"  {f.name}: {before/1024:>6.0f}KB -> {after/1024:>5.0f}KB")
    print(f"\n  TOTAL: {total_before/1024/1024:.2f}MB -> {total_after/1024/1024:.2f}MB "
          f"({100*(1-total_after/total_before):.0f}% smaller)")


if __name__ == "__main__":
    main()
