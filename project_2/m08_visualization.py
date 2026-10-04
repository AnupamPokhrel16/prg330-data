"""Module 8: Matplotlib visualization - charts built from Module 7's real analysis output."""
import numpy as np
import matplotlib.pyplot as plt


def plot_avg_aqi_by_city(city_summary_df, show=True):
    plt.figure(figsize=(9, 5))
    bars = plt.bar(city_summary_df.index, city_summary_df["AQI"], color="steelblue", edgecolor="white")
    plt.bar_label(bars, fmt="%.1f", padding=3)
    plt.title("Average AQI by City (2024)")
    plt.xlabel("city")
    plt.ylabel("average AQI (0-500 scale)")
    plt.xticks(rotation=20)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    if show:
        plt.show()


def plot_monthly_trend(monthly_series, show=True):
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    plt.figure(figsize=(9, 5))
    plt.plot(month_names, monthly_series.values, marker="o", color="darkorange")
    plt.title("Average AQI by Month (2024, All Cities)")
    plt.xlabel("month")
    plt.ylabel("average AQI (0-500 scale)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    if show:
        plt.show()


def plot_category_pie(category_counts, show=True):
    plt.figure(figsize=(7, 7))
    plt.pie(category_counts.values, labels=category_counts.index, autopct="%1.1f%%",
            colors=["mediumseagreen", "gold", "darkorange", "crimson"][:len(category_counts)],
            shadow=True, textprops={"color": "black"})
    plt.title("Share of Hours in Each AQI Category")
    if show:
        plt.show()


def plot_pm10_vs_aqi(df, correlation, show=True):
    slope, intercept = np.polyfit(df["PM10"], df["AQI"], 1)
    trend_x = np.array([df["PM10"].min(), df["PM10"].max()])
    trend_y = slope * trend_x + intercept

    plt.figure(figsize=(9, 6))
    plt.scatter(df["PM10"], df["AQI"], s=4, alpha=0.25, color="seagreen", label="hourly readings")
    plt.plot(trend_x, trend_y, color="black", linewidth=1.5, label="linear trend")
    plt.title(f"PM10 vs AQI (correlation = {correlation:.2f})")
    plt.xlabel("PM10 (ug/m3)")
    plt.ylabel("AQI (0-500 scale)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    if show:
        plt.show()


def plot_overall_pollutants(df, show=True):
    overall = df[["CO", "NO2", "SO2", "O3", "PM2.5", "PM10"]].mean().round(1)
    plt.figure(figsize=(9, 5))
    bars = plt.bar(overall.index, overall.values, color="indianred", edgecolor="white")
    plt.bar_label(bars, fmt="%.1f", padding=3)
    plt.title("Average Pollutant Levels (2024, All Cities)")
    plt.xlabel("pollutant")
    plt.ylabel("average level")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    if show:
        plt.show()


if __name__ == "__main__":
    import matplotlib
    matplotlib.use("Agg")
    from m00_load_data import load_data_with_month
    from m07_pandas_numpy import clean_data, city_summary, monthly_summary

    df = clean_data(load_data_with_month())
    plot_avg_aqi_by_city(city_summary(df), show=False)
    plot_monthly_trend(monthly_summary(df), show=False)
    plot_overall_pollutants(df, show=False)
    print("All charts generated without error.")
