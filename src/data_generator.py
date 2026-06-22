import pandas as pd
import numpy as np

def generate_production_data(n_days=180, seed=42):
    np.random.seed(seed)

    dates = pd.date_range("2024-01-01", periods=n_days, freq="D")

    df = pd.DataFrame({
        "date": dates,
        "oil_bbl": np.random.normal(1000, 80, n_days).cumsum(),
        "water_cut": np.random.uniform(0.1, 0.4, n_days),
        "pressure": np.random.normal(2500, 50, n_days)
    })

    return df