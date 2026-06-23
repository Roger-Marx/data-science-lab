from src.data_generator import generate_production_data
from src.data_cleaner import clean_production_data
from src.features import add_production_features


def test_pipeline():

    df = generate_production_data()

    df = clean_production_data(df)

    df = add_production_features(df)

    assert "oil_ma_7" in df.columns