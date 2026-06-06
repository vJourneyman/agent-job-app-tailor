#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pyyaml>=6.0.3",
# ]
# ///
"""
YAML Validation Gate helper script.
Parses a target file path and raises detailed errors if the YAML syntax is invalid.
Exits with status 0 on success, 1 on validation error, and 2 on other exceptions.
"""

import sys
import argparse
import yaml

def main():
    parser = argparse.ArgumentParser(description="Validate YAML file syntax.")
    parser.add_argument("file_path", help="Path to the YAML file to validate")
    args = parser.parse_args()

    try:
        with open(args.file_path, 'r', encoding='utf-8') as f:
            yaml.safe_load(f)
        print("✓ YAML is valid.")
        sys.exit(0)
    except yaml.YAMLError as exc:
        print(f"✗ YAML syntax error in {args.file_path}:", file=sys.stderr)
        print(exc, file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"Error reading {args.file_path}: {exc}", file=sys.stderr)
        sys.exit(2)

if __name__ == '__main__':
    main()
