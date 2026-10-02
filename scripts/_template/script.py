"""One-line summary of what this script does.

Author: Your Name
Date: YYYY-MM-DD
Usage: python script.py INPUT [--output OUT]
"""
import argparse


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="path to input file")
    parser.add_argument("--output", default="out.txt", help="path to output file")
    args = parser.parse_args()
    print(f"Reading {args.input}, writing {args.output}")


if __name__ == "__main__":
    main()
