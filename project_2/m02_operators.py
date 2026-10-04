"""Module 2: operators - arithmetic, comparison, logical and assignment, on two real rows."""
from m00_load_data import load_data
from m01_variables import get_worst_hour, get_best_hour, unpack_record


def arithmetic_demo(worst, best):
    pm_total_worst = worst["pm25_level"] + worst["pm10_level"]        # addition
    pm_difference_worst = worst["pm10_level"] - worst["pm25_level"]   # subtraction
    aqi_doubled_best = best["aqi_value"] * 2                           # multiplication
    aqi_halved_worst = worst["aqi_value"] / 2                          # division
    aqi_mod_worst = int(worst["aqi_value"]) % 50                       # modulus
    return {
        "pm_total_worst": pm_total_worst,
        "pm_difference_worst": pm_difference_worst,
        "aqi_doubled_best": aqi_doubled_best,
        "aqi_halved_worst": aqi_halved_worst,
        "aqi_mod_worst": aqi_mod_worst,
    }


def comparison_demo(worst, best):
    return {
        "worst_aqi_gt_best_aqi": worst["aqi_value"] > best["aqi_value"],
        "worst_city_ne_best_city": worst["record_city"] != best["record_city"],
        "worst_pm10_ge_100": worst["pm10_level"] >= 100,
    }


def logical_demo(worst):
    pm25_high = worst["pm25_level"] > 35
    pm10_high = worst["pm10_level"] > 150
    return {
        "both_high_and": pm25_high and pm10_high,
        "either_high_or": pm25_high or pm10_high,
        "not_calm": not (worst["aqi_value"] <= 50),
    }


def assignment_demo(worst, best):
    running_total = 0
    running_total += worst["aqi_value"]
    running_total += best["aqi_value"]
    running_total_scaled = running_total
    running_total_scaled *= 10
    return running_total, running_total_scaled


if __name__ == "__main__":
    df = load_data()
    worst = unpack_record(get_worst_hour(df))
    best = unpack_record(get_best_hour(df))
    print("Worst hour:", worst["record_city"], worst["record_date"], "AQI =", worst["aqi_value"])
    print("Best hour :", best["record_city"], best["record_date"], "AQI =", best["aqi_value"])
    print()
    print("Arithmetic:", arithmetic_demo(worst, best))
    print("Comparison:", comparison_demo(worst, best))
    print("Logical   :", logical_demo(worst))
    print("Assignment:", assignment_demo(worst, best))
