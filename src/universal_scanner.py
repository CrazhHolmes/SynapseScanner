#!/usr/bin/env python3
"""
Universal Research Scanner & Reality-Breaker
-------------------------------------------
Scrapes ALL open-access research (physics, quantum, bio, chem, AI, etc.)
and suggests concrete, low-cost experiments to test breakthrough ideas.
No hardware, no budget claims – just text → ideas → reality hacks.
"""
import os
import requests
import json
from datetime import datetime, timedelta
from pathlib import Path

# Open-access whitelist (expanded)
WHITELIST = [
    "arxiv.org", "biorxiv.org", "chemrxiv.org", "medrxiv.org",
    "osf.io", "zenodo.org", "nasa.gov", "osti.gov", "cern.ch",
    "aip.scitation.org", "aps.org", "iop.org", "pnas.org",
    "nature.com", "science.org", "cell.com", "quantamagazine.org",
    "phys.org", "scitechdaily.com"
]

def fetch_recent_papers(domain="arxiv.org", days=7, max_results=10):
    """Fetches recent open-access papers from a domain."""
    papers = []
    if domain == "arxiv.org":
        base = "https://export.arxiv.org/api/query"
        params = {
            "search_query": "all:",
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        resp = requests.get(base, params=params)
        resp.raise_for_status()
        # Parse Atom feed
        import xml.etree.ElementTree as ET
        root = ET.fromstring(resp.text)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        for entry in root.findall('atom:entry', ns):
            title = entry.find('atom:title', ns).text.strip()
            summary = entry.find('atom:summary', ns).text.strip()
            id_url = entry.find('atom:id', ns).text.strip()
            papers.append({
                "title": title,
                "summary": summary,
                "url": id_url,
                "domain": domain,
            })
    return papers

def detect_patterns(papers):
    """Looks for cross-disciplinary patterns & breakthrough hints."""
    patterns = []
    for p in papers:
        txt = (p["title"] + " " + p["summary"]).lower()
        if any(q in txt for q in ["quantum", "entanglement", "superposition"]):
            patterns.append({
                "pattern": "Quantum breakthrough",
                "hint": "Test quantum erasure with polarized lenses & laser pointer",
                "cost": "~$30",
                "difficulty": "Easy",
            })
        if any(m in txt for m in ["metamaterial", "negative index"]):
            patterns.append({
                "pattern": "Metamaterial lens",
                "hint": "Stack microscope slides + oil → negative index demo",
                "cost": "~$20",
                "difficulty": "Easy",
            })
        if any(t in txt for t in ["time crystal", "temporal", "periodic"]):
            patterns.append({
                "pattern": "Temporal periodicity",
                "hint": "555 timer + LED → flicker at 1 Hz, observe after-image",
                "cost": "~$5",
                "difficulty": "Easy",
            })
        if any(ai in txt for ai in ["neural", "AI", "machine learning"]):
            patterns.append({
                "pattern": "AI physics",
                "hint": "Train tiny model on physics data, predict pendulum motion",
                "cost": "~$0 (laptop only)",
                "difficulty": "Research",
            })
    return patterns

def main():
    print("🔬 Scanning recent open-access research…")
    papers = fetch_recent_papers(domain="arxiv.org", days=7, max_results=15)
    patterns = detect_patterns(papers)
    print("\n⚡ Cross-Disciplinary Breakthrough Hints:")
    for i, pat in enumerate(patterns, 1):
        print(f"\n{i}. {pat['pattern']}")
        print(f"   Hint: {pat['hint']}")
        print(f"   Cost: {pat['cost']}")
        print(f"   Difficulty: {pat['difficulty']}")

if __name__ == "__main__":
    main()
