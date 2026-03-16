#!/usr/bin/env python3
"""Convert JLCPCB positions CSV to NextPCB CPL format.

Reads production/positions.csv, excludes test points/DNP parts,
and outputs a NextPCB-compatible CPL file.

Usage: python3 scripts/generate_nextpcb_cpl.py
Output: production/nextpcb_cpl.csv
"""

import csv
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
POS_CSV = PROJECT_DIR / "production" / "positions.csv"
OUTPUT_CSV = PROJECT_DIR / "production" / "nextpcb_cpl.csv"

# Designators to exclude from placement
EXCLUDE_PREFIXES = {"TP"}  # Test points


def main():
    rows = []
    with open(POS_CSV, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            desig = row["Designator"].strip()
            # Skip test points
            prefix = "".join(c for c in desig if c.isalpha())
            if prefix in EXCLUDE_PREFIXES:
                continue
            rows.append({
                "Designator": desig,
                "Mid X": row["Mid X"].strip(),
                "Mid Y": row["Mid Y"].strip(),
                "Rotation": row["Rotation"].strip(),
                "Layer": row["Layer"].strip().capitalize(),  # top -> Top, bottom -> Bottom
            })

    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Designator", "Mid X", "Mid Y", "Rotation", "Layer"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"NextPCB CPL saved to: {OUTPUT_CSV}")
    print(f"Total placements: {len(rows)}")


if __name__ == "__main__":
    main()
