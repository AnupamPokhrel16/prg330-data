"""Module 0: shared data loader - reused by every other module in this project.

Every function in this project reads from the real Air_Quality.csv file. Nothing in
this module (or any module that imports it) is hand-typed or synthetic data.
"""
import pandas as pd

DATA_PATH = "Air_Quality.csv"


def load_data(path=DATA_PATH):
    """Load the raw Air Quality CSV into a DataFrame, exactly as recorded."""
    return pd.read_csv(path)


def load_data_with_month(path=DATA_PATH):
    """Load the CSV, parse Date into a real datetime, and add a Month column."""
    df = load_data(path)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.month
    return df


if __name__ == "__main__":
    df = load_data()
    print("Loaded", df.shape[0], "rows and", df.shape[1], "columns from", DATA_PATH)
    print(df.head())
