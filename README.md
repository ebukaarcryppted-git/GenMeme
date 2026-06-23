# GenMeme — GenLayer Meme Generator

> Create shareable Web3 memes with **Mochi**, GenLayer's official mascot.

**[Live Demo](https://github.com/ebukaarcryppted-git/GenMeme)** · Built for the GenLayer community

---

## What It Does

GenMeme is a browser-based meme generator built for [GenLayer](https://www.genlayer.com/) — the Intelligent Blockchain platform. Upload any photo, pick a Mochi pose, then **drag and zoom** Mochi anywhere on your image to compose the perfect meme. Download the result as a PNG, copy it to your clipboard, or share it straight to X.

No backend. No uploads. Everything runs in your browser.

---

## Features

- **Photo Upload** — drag-and-drop or click to load any image into the live preview
- **11 Mochi Poses** — bundled transparent PNGs of GenLayer's official mascot
- **Drag To Position** — click and drag Mochi anywhere on the canvas
- **Zoom On Cursor** — mouse wheel zoom anchored on the pointer, plus `+`, `−`, and `Reset` buttons
- **Per-Pose State** — each Mochi remembers its own position and zoom when you switch
- **Custom Mochi** — upload your own PNG to use as the overlay
- **PNG Export** — download at full photo resolution (capped at 1920px)
- **Copy to Clipboard** — instant paste anywhere
- **Share on X** — one-click tweet with pre-filled hashtags

---

## Tech Stack

| Layer | Choice |
|---|---|
| Runtime | Vanilla HTML5 + CSS + JS — zero dependencies |
| Canvas | HTML5 Canvas API (drag, zoom, composition, PNG export) |
| Input | Pointer Events API (mouse + touch + pen, all unified) |
| Fonts | Space Grotesk (display) + Inter (body) via Google Fonts |
| Assets | 11 transparent Mochi PNGs bundled locally in `assets/mochi/` |
| Preprocessing | `scripts/clean_mochi.py` — flood-fill alpha stripper for new poses |

---

## Design System

- **Background** — `#07191E` Deep Onyx
- **Accent** — `#02F5A1` Spring Green
- **Text** — `#FFFFFF` only
- Zero gradients · Zero shadows · Transform-only animations
- Swiss Modernism + Exaggerated Minimalism aesthetic
- Hairline grid backdrop · Corner tick marks · Infinite marquee ticker

---

## How to Run Locally

```bash
# Clone the repo
git clone https://github.com/ebukaarcryppted-git/GenMeme.git
cd GenMeme

# Serve with any static server
python -m http.server 3333
# then open http://localhost:3333
```

No build step. No `npm install`. Open `index.html` through any static server.

---

## Adding More Mochi Poses

Drop a new PNG into `assets/mochi/`, named `12.png`, `13.png`, etc. Then:

```bash
# Strip white backgrounds and tight-crop in place
python scripts/clean_mochi.py
```

Finally bump the `length: 11` in the `MOCHILIST` array inside `index.html` to match the new count.

---

## Project Structure

```
GenMeme/
├── index.html              # entire app — HTML, CSS, and JS in one file
├── assets/
│   └── mochi/              # 11 transparent Mochi pose PNGs
└── scripts/
    └── clean_mochi.py      # strip white bg + tight-crop helper
```

---

## About GenLayer

[GenLayer](https://www.genlayer.com/) is the world's first Intelligent Blockchain — combining smart contracts with AI to create Intelligent Contracts that can access the internet, process natural language, and make subjective decisions. Mochi is GenLayer's official mascot.

- Docs: [docs.genlayer.com](https://docs.genlayer.com)
- GitHub: [github.com/genlayer-foundation](https://github.com/genlayer-foundation)
- X: [@GenLayer](https://x.com/GenLayer)

---

## License

MIT
