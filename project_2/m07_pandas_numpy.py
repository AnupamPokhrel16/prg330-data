"""Module 7: Pandas + NumPy analysis - cleaning and the full 52,704-row analysis.

This is the biggest module because, in the course material this project follows,
data cleaning and the Pandas/NumPy analysis are taught together as one unit. Every
number here comes from the real, full dataset -- nothing is sampled or invented.
"""
import numpy as np
import pandas as pd
from m00_load_data import load_data_with_month

CLEANED_PATH = "air_quality_cleaned_data.csv"


def missing_value_summary(df):
    """Count and percentage of missing values in every column."""
    counts = df.isnull().sum()
    percent = (counts / len(df) * 100).round(2)
    return pd.DataFrame({"missing_count": counts, "missing_percent": percent})


def co2_availability_by_month(df, city):
    """CO2 readings-present vs readings-total by month, for one real city."""
    city_df = df[df["City"] == city]
    present = city_df.groupby("Month")["CO2"].apply(lambda col: col.notnull().sum())
    total = city_df.groupby("Month")["CO2"].size()
    return pd.DataFrame({"readings_present": present, "readings_total": total})


def co2_usable_window(df):
    """When CO2 actually starts being recorded, and the city averages in that window."""
    available = df[df["CO2"].notnull()]
    return {
        "earliest": available["Date"].min(),
        "latest": available["Date"].max(),
        "rows": len(available),
        "percent_of_all": round(len(available) / len(df) * 100, 1),
        "avg_by_city": available.groupby("City")["CO2"].mean().round(1),
    }


def classify_aqi(aqi):
    """Same EPA-style classifier used in Module 3, reapplied here at full dataset scale."""
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


def clean_data(df):
    """Add the AQI category, high-pollution flag, and PM total columns."""
    df = df.copy()
    df["AQI Category"] = df["AQI"].apply(classify_aqi)
    df["High Pollution"] = (df["PM2.5"] > 35) & (df["PM10"] > 150)
    df["PM_Total"] = df["PM2.5"] + df["PM10"]
    return df


def save_cleaned(df, path=CLEANED_PATH):
    """File output: save the cleaned DataFrame as a reusable project output."""
    df.to_csv(path, index=False)
    return path


def city_summary(df):
    """Average pollutant levels and AQI by city, worst to best."""
    cols = ["CO", "NO2", "SO2", "O3", "PM2.5", "PM10", "AQI"]
    return df.groupby("City")[cols].mean().round(2).sort_values("AQI", ascending=False)


def monthly_summary(df):
    """Average AQI by month, across all six cities."""
    return df.groupby("Month")["AQI"].mean().round(2)


def top_high_aqi_hours(df, threshold=100, top_n=10):
    """Count of hours over the threshold, and the single worst top_n rows."""
    high = df[df["AQI"] > threshold]
    worst = high[["Date", "City", "AQI", "PM2.5", "PM10"]].sort_values("AQI", ascending=False).head(top_n)
    return len(high), worst


def pollutant_correlations(df):
    """Correlation of every pollutant with AQI, strongest first."""
    cols = ["CO", "NO2", "SO2", "O3", "PM2.5", "PM10", "AQI"]
    return df[cols].corr()["AQI"].drop("AQI").sort_values(ascending=False).round(3)


def numpy_array_stats(df):
    """Mean/min/max/std for key pollutants, computed with NumPy arrays."""
    stats = {}
    for col in ["AQI", "PM2.5", "PM10", "CO", "NO2", "SO2", "O3"]:
        arr = df[col].to_numpy(dtype=float)
        stats[col] = {
            "mean": float(np.mean(arr)),
            "min": float(np.min(arr)),
            "max": float(np.max(arr)),
            "std": float(np.std(arr)),
        }
    return stats


def aqi_quartiles(df):
    """Q1/median/Q3, IQR, and the 1.5xIQR upper threshold for AQI, via NumPy."""
    arr = df["AQI"].to_numpy(dtype=float)
    q1, q2, q3 = np.percentile(arr, [25, 50, 75])
    iqr = q3 - q1
    upper = q3 + 1.5 * iqr
    above = int(np.sum(arr > upper))
    return {"q1": q1, "q2": q2, "q3": q3, "iqr": iqr, "upper_threshold": upper,
            "count_above": above, "total": int(arr.size)}


def threshold_counts(df):
    """Boolean-comparison counts on NumPy arrays for common pollution thresholds."""
    aqi = df["AQI"].to_numpy(dtype=float)
    pm25 = df["PM2.5"].to_numpy(dtype=float)
    pm10 = df["PM10"].to_numpy(dtype=float)
    return {
        "aqi_gt_100": int(np.sum(aqi > 100)),
        "pm25_gt_35": int(np.sum(pm25 > 35)),
        "pm10_gt_150": int(np.sum(pm10 > 150)),
    }


def numpy_corrcoef_check(df, column):
    """Independently re-verify a pandas correlation using np.corrcoef()."""
    a = df[column].to_numpy(dtype=float)
    b = df["AQI"].to_numpy(dtype=float)
    return float(np.corrcoef(a, b)[0, 1])


if __name__ == "__main__":
    df = load_data_with_month()
    print(missing_value_summary(df))
    print()

    df = clean_data(df)
    save_cleaned(df)
    print("Saved cleaned dataset to", CLEANED_PATH)
    print()

    print(city_summary(df))
    print()
    print(monthly_summary(df))
    print()
    print(pollutant_correlations(df))
