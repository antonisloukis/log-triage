#!/usr/bin/env python3
"""Simple log triage CLI.
Counts lines containing ERROR, WARNING, and INFO.
Exits with code 1 if any ERROR lines exist, otherwise 0.
"""
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Count ERROR/WARNING/INFO lines in a log file")
    parser.add_argument("path", help="Path to the log file")
    return parser.parse_args()


def main():
    args = parse_args()
    errors = warnings = infos = 0

    try:
        with open(args.path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                # Check in priority order so a line is counted once
                if "ERROR" in line:
                    errors += 1
                elif "WARNING" in line:
                    warnings += 1
                elif "INFO" in line:
                    infos += 1
    except FileNotFoundError:
        print(f"File not found: {args.path}", file=sys.stderr)
        sys.exit(2)
    except PermissionError:
        print(f"Permission denied: {args.path}", file=sys.stderr)
        sys.exit(2)

    print(f"Log summary for: {args.path}")
    print(f"ERROR:   {errors}")
    print(f"WARNING: {warnings}")
    print(f"INFO:    {infos}")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
