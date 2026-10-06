import csv
from collections import defaultdict
from datetime import datetime

input_file = "311_2024.csv"
output_file = "monthly_response_times.csv"

# key: (zipcode, month)
# value: [total_hours, count]
zipcode_stats = defaultdict(lambda: [0.0, 0])

# key: month
# value: [total_hours, count]
overall_stats = defaultdict(lambda: [0.0, 0])

with open(input_file, "r", newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)

    for row in reader:
        zipcode = row["Incident Zip"].strip()
        created = row["Created Date"].strip()
        closed = row["Closed Date"].strip()

        zipcode = row["Incident Zip"].strip()
        created = row["Created Date"].strip()
        closed = row["Closed Date"].strip()

        if not created or not closed:
         continue

        # Remove missing or invalid zipcodes
        if not zipcode.isdigit() or len(zipcode) != 5 or zipcode == "00000":
          continue

        try:
            created_dt = datetime.strptime(
                created,
                "%m/%d/%Y %I:%M:%S %p"
            )

            closed_dt = datetime.strptime(
                closed,
                "%m/%d/%Y %I:%M:%S %p"
            )
        except ValueError:
            continue

        response_hours = (
            closed_dt - created_dt
        ).total_seconds() / 3600

        if response_hours < 0:
            continue

        # FAQ says use the month in which the issue was closed
        month = closed_dt.month

        zipcode_stats[(zipcode, month)][0] += response_hours
        zipcode_stats[(zipcode, month)][1] += 1

        overall_stats[month][0] += response_hours
        overall_stats[month][1] += 1


with open(output_file, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)

    writer.writerow([
        "zipcode",
        "month",
        "avg_response_hours"
    ])

    for (zipcode, month), (total_hours, count) in sorted(zipcode_stats.items()):
        avg_hours = total_hours / count
        writer.writerow([zipcode, month, avg_hours])

    for month, (total_hours, count) in sorted(overall_stats.items()):
        avg_hours = total_hours / count
        writer.writerow(["ALL", month, avg_hours])

print(f"Created {output_file}")