# GenMeme — GenLayer Meme Generator

> Create shareable Web3 memes with **Mochi**, GenLayer's official mascot.

**[Live Demo](https://github.com/ebukaarcryppted-git/GenMeme)** · Built for the GenLayer community

---

## What It Does

GenMeme is a browser-based meme generator built for [GenLayer](https://www.genlayer.com/) — the Intelligent Blockchain platform. Upload your profile picture, pick a Mochi pose, and generate a crisp **1080×1080 meme** you can download, copy to clipboard, or share directly to X (Twitter).

No backend. No uploads. Everything runs in your browser.

---

## Features

- **PFP Upload** — drag-and-drop or click to upload your profile picture
- **9 Mochi Poses** — choose from GenLayer's official mascot artwork (renders, concept art, stickers)
- **4 Meme Templates**
  - `Side by Side` — you and Mochi, side by side
  - `Certified` — certified stamp layout
  - `GM Ser` — good morning Web3 energy
  - `When…` — classic reaction format
- **Custom Captions** — add your own text to each template
- **1080×1080 Export** — full-resolution PNG download
- **Copy to Clipboard** — instant paste anywhere
- **Share on X** — one-click tweet with pre-filled hashtags

---

## Tech Stack

| Layer | Choice |
|---|---|
| Runtime | Vanilla HTML5 + CSS + JS — zero dependencies |
| Canvas | HTML5 Canvas API (meme composition + export) |
| Fonts | Space Grotesk (display) + Inter (body) via Google Fonts |
| Image CDN | [wsrv.nl](https://wsrv.nl/) — resizes 4000×4000 Mochi PNGs to WebP for instant display |
| Mascot Assets | [genlayer-foundation/genlayer-mascot](https://github.com/genlayer-foundation/genlayer-mascot) |

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

No build step. No `npm install`. Open `index.html` in a browser and it works.

---

## Project Structure

```
GenMeme/
└── index.html      # entire app — HTML, CSS, and JS in one file
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
