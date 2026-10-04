"""Module 9: conclusion - findings generated live from the real numbers Module 7 produced.

No number in this module is hardcoded. Every finding is formatted from whatever the
city_summary / monthly_summary / correlation tables actually contain when this runs.
"""


def major_findings(city_summary_df, monthly_series, high_aqi_count, total_rows,
                    worst_event_city, worst_event_date, corr_series, co2_info):
    worst_city = city_summary_df.index[0]
    worst_aqi = city_summary_df["AQI"].iloc[0]
    best_city = city_summary_df.index[-1]
    best_aqi = city_summary_df["AQI"].iloc[-1]

    peak_month = int(monthly_series.idxmax())
    peak_value = monthly_series.max()
    low_month = int(monthly_series.idxmin())
    low_value = monthly_series.min()

    top_pollutant = corr_series.index[0]
    top_corr = corr_series.iloc[0]

    lines = [
        f"1. {worst_city} has the worst average air quality in this dataset (AQI {worst_aqi}); "
        f"{best_city} has the best (AQI {best_aqi}).",

        f"2. AQI peaks in month {peak_month} (avg {peak_value}) and is lowest in month "
        f"{low_month} (avg {low_value}).",

        f"3. {high_aqi_count} of {total_rows} hours ({high_aqi_count / total_rows * 100:.2f}%) "
        f"exceed AQI 100; the single worst hours are concentrated in {worst_event_city} "
        f"around {worst_event_date}.",

        f"4. {top_pollutant} is the strongest numerical driver of AQI in this dataset, "
        f"correlating at r = {top_corr}.",

        f"5. CO2 is only usable from {co2_info['earliest']} to {co2_info['latest']} "
        f"({co2_info['percent_of_all']}% of all rows) -- kept out of the main year-long "
        f"comparison for that reason.",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    from m00_load_data import load_data_with_month
    from m07_pandas_numpy import (clean_data, city_summary, monthly_summary, top_high_aqi_hours,
                                   pollutant_correlations, co2_usable_window)

    df = clean_data(load_data_with_month())
    cs = city_summary(df)
    ms = monthly_summary(df)
    high_count, worst_rows = top_high_aqi_hours(df)
    worst_city_name = worst_rows.iloc[0]["City"]
    worst_date = worst_rows.iloc[0]["Date"]
    corr = pollutant_correlations(df)
    co2 = co2_usable_window(df)

    print(major_findings(cs, ms, high_count, len(df), worst_city_name, worst_date, corr, co2))
