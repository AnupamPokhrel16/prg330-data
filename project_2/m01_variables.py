"""Module 1: variables and data types - built from real rows of the dataset.

We never hand-type a sample record. The "worst" and "best" hours below are found by
filtering the real dataset (idxmax / idxmin on the real AQI column), not invented.
"""
from m00_load_data import load_data


def get_worst_hour(df):
    """Return the single real row with the highest AQI in the whole dataset."""
    worst_idx = df["AQI"].idxmax()
    return df.loc[worst_idx].to_dict()


def get_best_hour(df):
    """Return the single real row with the lowest AQI in the whole dataset."""
    best_idx = df["AQI"].idxmin()
    return df.loc[best_idx].to_dict()


def unpack_record(record):
    """Pull a record dict apart into individual named variables, showing each Python type."""
    record_date = str(record["Date"])          # str
    record_city = str(record["City"])          # str
    co_level = float(record["CO"])              # float
    co2_level = record["CO2"]                   # float (may be NaN)
    no2_level = float(record["NO2"])             # float
    so2_level = float(record["SO2"])             # float
    o3_level = float(record["O3"])               # float
    pm25_level = float(record["PM2.5"])          # float
    pm10_level = float(record["PM10"])           # float
    aqi_value = float(record["AQI"])             # float
    is_high_pollution_hour = aqi_value > 100     # bool

    return {
        "record_date": record_date,
        "record_city": record_city,
        "co_level": co_level,
        "co2_level": co2_level,
        "no2_level": no2_level,
        "so2_level": so2_level,
        "o3_level": o3_level,
        "pm25_level": pm25_level,
        "pm10_level": pm10_level,
        "aqi_value": aqi_value,
        "is_high_pollution_hour": is_high_pollution_hour,
    }


if __name__ == "__main__":
    df = load_data()
    worst = unpack_record(get_worst_hour(df))
    print("Worst recorded hour in the whole dataset:")
    for name, value in worst.items():
        print(f"  {name:22s} = {value!r:25}  ({type(value).__name__})")
