#!/usr/bin/env python3
"""
Simple CSV -> JSON expense summariser.
CSV expected columns: date,category,amount (amount as number)
Usage: python expense_summary.py expenses.csv output.json
"""
import csv
import json
import sys
from collections import defaultdict
from decimal import Decimal


def summarize(csv_path):
    totals = defaultdict(Decimal)
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            amt = Decimal(row.get("amount", "0"))
            cat = row.get("category", "unknown").strip()
            totals[cat] += amt
    # convert Decimals -> floats for JSON
    return {k: float(v) for k, v in totals.items()}


def main():
    if len(sys.argv) < 3:
        print("Usage: python expense_summary.py input.csv output.json")
        sys.exit(2)
    csv_path, out_path = sys.argv[1], sys.argv[2]
    summary = summarize(csv_path)
    with open(out_path, "w", encoding="utf-8") as out:
        json.dump({"by_category": summary}, out, indent=2)
    print(f"Wrote summary to {out_path}")


if __name__ == "__main__":
    main()
