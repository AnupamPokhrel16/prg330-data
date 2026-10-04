"""Module 3: conditional statements - if / elif / else, applied to real AQI values."""
from m00_load_data import load_data
from m01_variables import get_worst_hour, get_best_hour, unpack_record


def classify_aqi(aqi):
    """Return the EPA-style category name for a given AQI value."""
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"


def high_pollution_condition(pm25, pm10):
    """True only when both PM2.5 and PM10 are elevated at the same time."""
    if pm25 > 35 and pm10 > 150:
        return True
    else:
        return False


if __name__ == "__main__":
    df = load_data()
    worst = unpack_record(get_worst_hour(df))
    best = unpack_record(get_best_hour(df))
    for label, record in [("Worst hour", worst), ("Best hour", best)]:
        category = classify_aqi(record["aqi_value"])
        flagged = high_pollution_condition(record["pm25_level"], record["pm10_level"])
        print(f"{label}: {record['record_city']} {record['record_date']} "
              f"AQI={record['aqi_value']:.1f} -> {category}  (high pollution: {flagged})")
