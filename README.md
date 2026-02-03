# SynapseScanner

**A clean Python CLI that searches open-access research papers and surfaces cross-disciplinary breakthrough patterns.**

![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![MIT License](https://img.shields.io/badge/license-MIT-green.svg)
![CI](https://github.com/CrazhHolmes/SynapseScanner/actions/workflows/ci.yml/badge.svg)

---

## What it does

SynapseScanner fetches recent papers from arXiv (with more sources planned), scans them for cross-disciplinary patterns (quantum, metamaterials, AI, temporal physics), and suggests concrete low-cost experiments you can try at home.

## Demo

<!-- Captured from a live run against the arXiv API -->
```
  ╭───────────────────────────────────╮
  │       SynapseScanner v1.0.0       │
  │   Quantum Research Intelligence   │
  ╰───────────────────────────────────╯

  ✔ Found 15 papers
  arxiv.org/abs/1104.0917v1  ━━━━━━━━━━━━━━━━━━━━━━━━  15/15  100%

  ╭── Discoveries ─────────────────────────────────────────────╮
  │  ⚛  Quantum breakthrough
  │     Test quantum erasure with polarized lenses & laser pointer
  │     ~$30 · Easy
  ╰────────────────────────────────────────────────────────────╯

  ⚛  Quantum breakthrough
    Quantum erasure can be demonstrated with inexpensive optical
    components, opening a low-cost pathway for teaching advanced
    quantum-mechanics experiments in undergraduate labs.

  keywords  entanglement ⣿⣿⣿  topology ⣿⣿⣿

  ✔ Done · 15 papers · 1 patterns · 0.7s
  ⚡ github.com/CrazhHolmes/SynapseScanner
```

## Installation

**From source (recommended):**

```bash
git clone https://github.com/CrazhHolmes/SynapseScanner.git
cd SynapseScanner
pip install .
```

**Or run directly without installing:**

```bash
git clone https://github.com/CrazhHolmes/SynapseScanner.git
cd SynapseScanner
pip install -r synapsescanner/requirements.txt
python -m synapsescanner.universal_scanner
```

## Quick start

```bash
# Default: fetch 15 recent papers from arXiv
synapsescanner

# Fetch fewer papers for a quick scan
synapsescanner --max-results 5

# Greyscale theme
synapsescanner --noir

# Matrix rain easter egg
synapsescanner --matrix

# Show CLI reference card
synapsescanner --cheat
```

## Full usage

```
synapsescanner [--max-results N] [--noir] [--matrix] [--cheat]
```

| Flag | Effect |
|------|--------|
| `--max-results N` | Number of papers to fetch (default: 15) |
| `--noir` | Greyscale mode -- no color |
| `--matrix` | Matrix rain easter egg before scanning |
| `--cheat` | Print CLI reference card and exit |

### Environment variables

| Variable | Equivalent flag | Description |
|----------|----------------|-------------|
| `SYNAPSE_MATRIX=1` | `--matrix` | Enable Matrix-rain easter egg |
| `SYNAPSE_NOIR=1` | `--noir` | Force greyscale colors |

Environment variables and flags can be combined:

```bash
SYNAPSE_NOIR=1 synapsescanner --max-results 7
```

## Output features

- **Clickable paper URLs** -- Click a paper link in the progress bar to open it in your browser (OSC 8 hyperlinks, works in Windows Terminal, iTerm2, GNOME Terminal)
- **Braille sparklines** -- Keyword frequencies rendered as compact `⣀⣄⣤⣦⣶⣷⣿` bars using Unicode Braille patterns (U+2800)
- **True-color gradient banner** -- 24-bit RGB interpolation from cyan to purple (not the 256-color palette)
- **Discovery explanations** -- Each detected pattern includes a short "why it matters" paragraph
- **In-place progress bar** -- Single-line rewrite with cursor hide/show, no scroll spam
- **Crash-safe cursor** -- `atexit` handler guarantees the terminal cursor is restored even on unexpected exit

## Pattern detection

SynapseScanner scans paper titles and abstracts for four cross-disciplinary pattern categories:

| Pattern | Keywords detected | Suggested experiment | Cost |
|---------|------------------|---------------------|------|
| Quantum breakthrough | quantum, entanglement, superposition | Quantum erasure with polarized lenses & laser pointer | ~$30 |
| Metamaterial lens | metamaterial, negative index | Stack microscope slides + oil for negative index demo | ~$20 |
| Temporal periodicity | time crystal, temporal, periodic | 555 timer + LED at 1 Hz | ~$5 |
| AI physics | neural, AI, machine learning | Train tiny model on pendulum data | ~$0 |

## Data sources

**Currently active:**

| Source | URL | Status |
|--------|-----|--------|
| arXiv | arxiv.org | Active -- fetches via Atom API |

**In whitelist (planned):**

bioRxiv, chemRxiv, medRxiv, OSF, Zenodo, NASA Technical Reports, OSTI, CERN, AIP, APS, IOP, PNAS, Nature, Science, Cell, Quanta Magazine, Phys.org, SciTechDaily

## Windows / PowerShell shortcut

Add this function to your PowerShell `$PROFILE` for a shorter command:

```powershell
function synapse {
    param(
        [int]$MaxResults = 15,
        [switch]$Matrix,
        [switch]$Noir,
        [switch]$Cheat
    )
    $flags = @("--max-results", $MaxResults)
    if ($Matrix) { $flags += "--matrix" }
    if ($Noir) { $flags += "--noir" }
    if ($Cheat) { $flags += "--cheat" }
    python -m synapsescanner.universal_scanner @flags
}
```

Then run:

```powershell
synapse                          # default scan
synapse -MaxResults 5            # quick scan
synapse -Matrix                  # matrix rain
synapse -Noir                    # greyscale
synapse -Cheat                   # reference card
```

## CMD shortcut (batch file)

Save as `synapse.bat` somewhere on your `PATH`:

```bat
@echo off
python -m synapsescanner.universal_scanner %*
```

Then run:

```cmd
synapse --max-results 5
synapse --matrix
```

## Contributing

- Add new data sources by extending `fetch_recent_papers()` in `synapsescanner/universal_scanner.py`
- Add new pattern categories in `detect_patterns()` with matching entries in `_ICONS` and `_EXPLANATIONS` in `synapsescanner/cli_extras.py`
- The open-access source whitelist is in `WHITELIST` in `synapsescanner/universal_scanner.py`

PRs welcome.

## Requirements

- Python 3.9+
- `requests` (only runtime dependency beyond stdlib)

## License

MIT -- fork, hack, cite.
