import argparse
import sys
from .loader import load_from_files
from .reports import REPORTS
from .render import render_table
from typing import Sequence


def parse_args(argv: Sequence[str] | None = None):
    parser = argparse.ArgumentParser(description="Dev performance reports")
    parser.add_argument("--files", nargs="+", required=True, help="CSV files")
    parser.add_argument("--report", required=True, help="Report name")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)

    if args.report not in REPORTS:
        print(f"Unknown report: {args.report}", file=sys.stderr)
        return 2

    try:
        records = load_from_files(args.files)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 3

    report_fn = REPORTS[args.report]
    rows = report_fn(records)

    if args.report == "performance":
        render_table(rows, headers=["position", "avg_performance"])
    else:
        # generic render if new reports appear
        if rows:
            render_table(rows, headers=list(rows[0].keys()))
        else:
            print("No data to show.")
    return 0
