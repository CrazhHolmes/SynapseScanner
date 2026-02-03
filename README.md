# SynapseScanner -- Universal Research Scanner

**Fast, click-through CLI for open-access papers**

![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![MIT License](https://img.shields.io/badge/license-MIT-green.svg)
![CI](https://github.com/CrazhHolmes/SynapseScanner/actions/workflows/ci.yml/badge.svg)

---

## What it does

- Scrapes open-access research from **arXiv**, bioRxiv, Zenodo, and 20+ sources
- Detects cross-disciplinary breakthrough patterns (quantum, metamaterials, AI, temporal physics)
- Suggests **concrete, low-cost experiments** with cost estimates
- Displays results with 24-bit true-color gradients, OSC 8 clickable paper links, and Braille sparklines

## Demo

<!-- Replace with your own recording: asciinema rec demo.cast && agg demo.cast demo.gif -->
```
  ╭───────────────────────────────────╮
  │     SynapseScanner v1.0.0        │
  │  Quantum Research Intelligence    │
  ╰───────────────────────────────────╯

  ✔ Found 15 papers
  arxiv.org/abs/2501.12345  ━━━━━━━━━━━━━━━━━━━━━━━━  15/15  100%

  ╭── Discoveries ──────────────────────────────────────────╮
  │  ⚛  Quantum breakthrough                               │
  │     Test quantum erasure with polarized lenses...       │
  │     ~$30 · Easy                                         │
  ╰─────────────────────────────────────────────────────────╯

  keywords  quantum ⣿⣿⣿  topology ⣶⣶⣶  spin ⣤⣤⣤

  ✔ Done · 15 papers · 2 patterns · 1.8s
  ⚡ github.com/CrazhHolmes/SynapseScanner
```

## Quick start

```bash
git clone https://github.com/CrazhHolmes/SynapseScanner.git
cd SynapseScanner
pip install -r src/requirements.txt
python src/universal_scanner.py
```

## CLI flags

| Flag | Effect |
|------|--------|
| `--max-results N` | Papers to fetch (default 15) |
| `--noir` | Greyscale mode |
| `--matrix` | Matrix rain easter egg |
| `--cheat` | Show CLI reference |

Paper URLs in the progress bar are **clickable** in Windows Terminal, iTerm2, and GNOME Terminal (OSC 8 hyperlinks).

## Unique CLI tricks

- **24-bit true-color gradients** -- smooth cyan-to-purple banner (not the 256-color palette)
- **OSC 8 terminal hyperlinks** -- click a paper URL to open it in your browser
- **Braille U+2800 sparklines** -- ultra-compact keyword frequency bars
- **In-place line rewrites** -- flicker-free progress bar
- **Cursor hide/show + atexit** -- clean progress, cursor always restored on crash

## Requirements

- Python 3.9+
- `requests` (the only runtime dependency that isn't stdlib)

```bash
pip install -r src/requirements.txt
```

## License

MIT -- fork, hack, cite.
