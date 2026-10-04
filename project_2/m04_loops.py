"""Module 4: loops - for, for-with-condition, and while, over a real 12-row sample.

The 12-row sample is pulled by filtering the real dataset for two real timestamps
(one per city, at each timestamp) -- it is never hand-typed.
"""
import pandas as pd
from m00_load_data import load_data

SAMPLE_DATES = ["2024-02-11 16:00:00+00:00", "2024-12-29 22:00:00+00:00"]


def get_sample_rows(df):
    """Pull the same real hour from every city, for two real dates: a 12-row sample
    selected from the actual dataset by filtering, not typed in by hand."""
    mask = df["Date"].astype(str).isin(SAMPLE_DATES)
    sample = df[mask].sort_values(["Date", "City"]).reset_index(drop=True)
    return sample.to_dict("records")


def total_and_average_aqi(records):
    """A basic for loop: add up AQI and count records by hand."""
    total = 0.0
    count = 0
    for rec in records:
        total += rec["AQI"]
        count += 1
    average = total / count if count else 0
    return total, average


def flag_high_aqi(records, threshold=50):
    """A for loop with a condition inside: collect every record above the threshold."""
    flagged = []
    for rec in records:
        if rec["AQI"] > threshold:
            flagged.append(rec)
    return flagged


def find_worst_without_max(records):
    """Find the worst record using a loop and a comparison, without calling max()."""
    worst = records[0]
    for rec in records:
        if rec["AQI"] > worst["AQI"]:
            worst = rec
    return worst


def first_missing_co2(records):
    """A while loop: stop as soon as the first record with a missing CO2 value is found."""
    index = 0
    found = False
    while index < len(records) and not found:
        if pd.isna(records[index]["CO2"]):
            found = True
        else:
            index += 1
    return records[index] if found else None


if __name__ == "__main__":
    df = load_data()
    sample = get_sample_rows(df)
    print("Sample size:", len(sample))

    total, average = total_and_average_aqi(sample)
    print("Total AQI:", round(total, 2), " Average AQI:", round(average, 2))

    high = flag_high_aqi(sample)
    print("High-AQI (>50) records:", len(high), "out of", len(sample))

    worst = find_worst_without_max(sample)
    print("Worst sample record:", worst["City"], worst["Date"], "AQI =", worst["AQI"])

    first_missing = first_missing_co2(sample)
    if first_missing:
        print("First record with missing CO2:", first_missing["City"], first_missing["Date"])
