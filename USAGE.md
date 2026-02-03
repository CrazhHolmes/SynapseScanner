# SynapseScanner Usage Guide

## Quick examples

```bash
# Search for a topic
synapsescanner "quantum entanglement"

# Limit results
synapsescanner "CRISPR" --max-results 5

# Fetch recent papers (no query)
synapsescanner

# Greyscale mode
synapsescanner "neural networks" --noir

# Matrix rain easter egg
synapsescanner "graph theory" --matrix

# Show help
synapsescanner --cheat
```

---

## Three ways to run

### 1. Installed command (recommended)

After `pip install .` from the repo folder:

```bash
synapsescanner "quantum entanglement"
synapsescanner "CRISPR" --max-results 5
synapsescanner --noir
```

### 2. Windows batch file

From the repo folder:

```cmd
cd C:\Users\bings\SynapseScanner
.\synapse.bat "quantum entanglement"
.\synapse.bat "CRISPR" --max-results 5
.\synapse.bat --cheat
```

### 3. Direct Python

```bash
python -m synapsescanner.universal_scanner "quantum entanglement"
python -m synapsescanner.universal_scanner "graph neural networks" --max-results 5
python -m synapsescanner.universal_scanner --noir
```

---

## PowerShell shortcut

The `synapse` function is installed in your PowerShell profile. Usage:

```powershell
synapse "quantum entanglement"
synapse "CRISPR" -MaxResults 5
synapse "neural networks" -Noir
synapse -Cheat
```

---

## All options

| Option | Description |
|--------|-------------|
| `[query]` | Search term (optional, fetches recent papers if omitted) |
| `--max-results N` | Number of papers to fetch (default: 15) |
| `--noir` | Greyscale mode |
| `--matrix` | Matrix rain easter egg |
| `--cheat` | Show CLI reference |

## Environment variables

| Variable | Effect |
|----------|--------|
| `SYNAPSE_MATRIX=1` | Same as `--matrix` |
| `SYNAPSE_NOIR=1` | Same as `--noir` |
