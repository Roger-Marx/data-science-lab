from src.data_generator import generate_production_data


def test_dataframe_shape():
    df = generate_production_data()

    assert len(df) == 180


def test_columns_exist():
    df = generate_production_data()

    expected_columns = [
        "date",
        "oil_bbl",
        "water_cut",
        "pressure"
    ]

    assert list(df.columns) == expected_columns


def test_seed_reproducibility():
    df1 = generate_production_data(seed=42)
    df2 = generate_production_data(seed=42)

    assert df1.equals(df2)