import argparse
import csv
import sys
from collections import defaultdict
from datetime import datetime, timedelta


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

    start_date = datetime.strptime(args.start, "%m/%d/%Y")
    end_date = datetime.strptime(args.end, "%m/%d/%Y") + timedelta(days=1)

    counts = defaultdict(int)

    with open(args.input, "r", newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            created = row["Created Date"]

            if not created:
                continue

            try:
                created_date = datetime.strptime(
                    created,
                    "%m/%d/%Y %I:%M:%S %p"
                )
            except ValueError:
                continue

            if start_date <= created_date < end_date:
                complaint_type = row["Complaint Type"]
                borough = row["Borough"]

                counts[(complaint_type, borough)] += 1

    if args.output:
        outfile = open(args.output, "w", newline="", encoding="utf-8")
    else:
        outfile = sys.stdout

    writer = csv.writer(outfile)
    writer.writerow(["complaint type", "borough", "count"])

    for (complaint_type, borough), count in sorted(counts.items()):
        writer.writerow([complaint_type, borough, count])

    if args.output:
        outfile.close()


if __name__ == "__main__":
    main()