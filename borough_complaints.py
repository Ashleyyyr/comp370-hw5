import argparse
import csv
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(
        description="Count complaint types by borough within a date range."
    )

    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Input CSV file"
    )

    parser.add_argument(
        "-s",
        "--start",
        required=True,
        help="Start date in MM/DD/YYYY format"
    )

    parser.add_argument(
        "-e",
        "--end",
        required=True,
        help="End date in MM/DD/YYYY format"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Optional output CSV file"
    )

    return parser.parse_args()


def main():
    args = parse_args()


if __name__ == "__main__":
    main()
