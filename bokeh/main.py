import csv
from collections import defaultdict

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import Select, ColumnDataSource
from bokeh.plotting import figure


DATA_FILE = "monthly_response_times.csv"


def load_data(filename):
    data = defaultdict(dict)

    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            zipcode = row["zipcode"]
            month = int(row["month"])
            avg_hours = float(row["avg_response_hours"])

            data[zipcode][month] = avg_hours

    return data


data = load_data(DATA_FILE)

zipcodes = sorted(z for z in data.keys() if z != "ALL")

zipcode1 = Select(
    title="Zipcode 1",
    value=zipcodes[0],
    options=zipcodes
)

zipcode2 = Select(
    title="Zipcode 2",
    value=zipcodes[1],
    options=zipcodes
)

months = list(range(1, 13))


def monthly_values(zipcode):
    return [data[zipcode].get(month, float("nan")) for month in months]


overall_source = ColumnDataSource(
    data={
        "month": months,
        "response_time": monthly_values("ALL")
    }
)

zipcode1_source = ColumnDataSource(
    data={
        "month": months,
        "response_time": monthly_values(zipcode1.value)
    }
)

zipcode2_source = ColumnDataSource(
    data={
        "month": months,
        "response_time": monthly_values(zipcode2.value)
    }
)

plot = figure(
    title="Monthly Average 311 Response Time by Zipcode",
    x_axis_label="Month",
    y_axis_label="Average Response Time (Hours)",
    width=800,
    height=500
)

plot.line(
    "month",
    "response_time",
    source=overall_source,
    line_width=2,
    legend_label="All Zipcodes"
)

plot.line(
    "month",
    "response_time",
    source=zipcode1_source,
    line_width=2,
    legend_label="Zipcode 1"
)

plot.line(
    "month",
    "response_time",
    source=zipcode2_source,
    line_width=2,
    legend_label="Zipcode 2"
)

plot.legend.location = "top_right"


def update(attr, old, new):
    zipcode1_source.data = {
        "month": months,
        "response_time": monthly_values(zipcode1.value)
    }

    zipcode2_source.data = {
        "month": months,
        "response_time": monthly_values(zipcode2.value)
    }


zipcode1.on_change("value", update)
zipcode2.on_change("value", update)

curdoc().add_root(
    column(
        zipcode1,
        zipcode2,
        plot
    )
)

curdoc().title = "NYC 311 Response Time Dashboard"
