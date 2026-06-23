"""Strip white background from each Mochi PNG and crop to the head bbox.

For every assets/mochi/N.png:
  - Flood-fill outward from the four image corners over near-white pixels,
    marking them transparent (this keeps any small white highlights INSIDE
    the character solid).
  - Soften the alpha at the contour to avoid hard pixel edges.
  - Crop tightly around the remaining opaque region.
  - Overwrite the original PNG.
"""

from PIL import Image
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "mochi"

# pixels with all RGB channels above this AND low color variance are "white"
WHITE_THRESH = 238
CHROMA_THRESH = 16  # max(R,G,B) - min(R,G,B)


def is_whiteish(r: int, g: int, b: int) -> bool:
    if r < WHITE_THRESH or g < WHITE_THRESH or b < WHITE_THRESH:
        return False
    return max(r, g, b) - min(r, g, b) <= CHROMA_THRESH


def process(path: Path) -> None:
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    px = img.load()

    visited = bytearray(w * h)
    q: deque[tuple[int, int]] = deque()

    # seed from every border pixel that is whiteish
    for x in range(w):
        for y in (0, h - 1):
            r, g, b, _ = px[x, y]
            if is_whiteish(r, g, b):
                idx = y * w + x
                if not visited[idx]:
                    visited[idx] = 1
                    q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            r, g, b, _ = px[x, y]
            if is_whiteish(r, g, b):
                idx = y * w + x
                if not visited[idx]:
                    visited[idx] = 1
                    q.append((x, y))

    # 4-way flood across whiteish pixels
    while q:
        x, y = q.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h:
                idx = ny * w + nx
                if visited[idx]:
                    continue
                r, g, b, _ = px[nx, ny]
                if is_whiteish(r, g, b):
                    visited[idx] = 1
                    q.append((nx, ny))

    # zero alpha on every visited pixel
    for y in range(h):
        for x in range(w):
            if visited[y * w + x]:
                r, g, b, _ = px[x, y]
                px[x, y] = (r, g, b, 0)

    # soft contour: any opaque pixel touching a transparent pixel gets alpha eased
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            # near contour?
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if px[nx, ny][3] == 0:
                    # if this pixel is itself near-white, push alpha down
                    if is_whiteish(r, g, b):
                        px[x, y] = (r, g, b, 0)
                    break

    # crop to opaque bbox
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)

    img.save(path, "PNG", optimize=True)


def main() -> None:
    files = sorted(SRC.glob("*.png"), key=lambda p: int(p.stem) if p.stem.isdigit() else 999)
    for f in files:
        before = f.stat().st_size
        process(f)
        after = f.stat().st_size
        print(f"  {f.name}: {before:>8} -> {after:>8} bytes")


if __name__ == "__main__":
    main()
