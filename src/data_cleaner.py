import pandas as pd


def clean_production_data(df):
    """
    Basic cleaning pipeline.
    """

    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])

    df = df.sort_values("date")

    df = df.drop_duplicates()

    return df