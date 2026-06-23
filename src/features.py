def add_production_features(df):

    df = df.copy()

    df["oil_ma_7"] = (
        df["oil_bbl"]
        .rolling(window=7)
        .mean()
    )

    return df