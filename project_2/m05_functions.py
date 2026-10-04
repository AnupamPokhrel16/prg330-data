"""Module 5: functions - reusable total/average/condition helpers, called on real data."""
from m00_load_data import load_data


def calculate_total(values):
    """Add up a list of numbers using a loop."""
    total = 0
    for v in values:
        total += v
    return total


def calculate_average(values):
    """Return the average of a list of numbers."""
    if len(values) == 0:
        return 0
    return calculate_total(values) / len(values)


def is_high_pollution(pm25, pm10, pm25_limit=35, pm10_limit=150):
    """Return True when both PM2.5 and PM10 exceed the given limits."""
    return pm25 > pm25_limit and pm10 > pm10_limit


def summarize_city_aqi(df, city):
    """Use calculate_total / calculate_average on every real AQI reading for one real city."""
    values = df.loc[df["City"] == city, "AQI"].tolist()
    return {
        "city": city,
        "count": len(values),
        "total": round(calculate_total(values), 2),
        "average": round(calculate_average(values), 2),
    }


if __name__ == "__main__":
    df = load_data()
    for city in sorted(df["City"].unique()):
        print(summarize_city_aqi(df, city))

    worst_row = df.loc[df["AQI"].idxmax()]
    print("High pollution at the dataset's worst hour:",
          is_high_pollution(worst_row["PM2.5"], worst_row["PM10"]))
