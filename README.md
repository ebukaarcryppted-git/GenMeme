# GenMeme — GenLayer Meme Generator

> Create shareable Web3 memes with **Mochi**, GenLayer's official mascot.

**[Live Demo](https://github.com/ebukaarcryppted-git/GenMeme)** · Built for the GenLayer community

---

## What It Does

GenMeme is a browser-based meme generator built for the GenLayer community. It lets anyone compose a shareable meme by overlaying Mochi, GenLayer's official mascot onto any photo, then downloading or sharing the result straight to X or anywhere.

---

## Features

- **Photo Upload** — Drag-and-drop or click-to-browse; loads instantly into the live canvas
- **11 Mochi Poses** — Transparent PNGs of GenLayer's mascot, displayed in a static tile grid
- **Drag To Position** — Click/touch and drag Mochi anywhere on the canvas
- **Zoom On Cursor** — Mouse wheel zoom anchored to pointer; + / − / Reset toolbar buttons
- **Per-Pose Memory** — Each Mochi pose remembers its own position and zoom independently
- **Custom Mochi** — upload your own PNG to use as the overlay
- **Meme Text** — Type text directly onto the meme; drag it anywhere on the canvas
- **Multi-line** — Text	Press Enter to break onto a new line
- **Text Styling** — 4 color options (white, yellow, green, red) + 4 font sizes (S / M / L / XL)
- **PNG Download** — Exports at full photo resolution (capped at 1920px)
- **Copy to Clipboard** — instant paste anywhere
- **Share on X** — Opens a pre-filled tweet with GenLayer hashtags

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

## About GenLayer

[GenLayer](https://www.genlayer.com/) is the world's first Intelligent Blockchain — combining smart contracts with AI to create Intelligent Contracts that can access the internet, process natural language, and make subjective decisions. Mochi is GenLayer's official mascot.

- Docs: [docs.genlayer.com](https://docs.genlayer.com)
- GitHub: [github.com/genlayer-foundation](https://github.com/genlayer-foundation)
- X: [@GenLayer](https://x.com/GenLayer)

---

## License

MIT
