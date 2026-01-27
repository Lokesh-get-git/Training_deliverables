import pandas as pd


def load_csv_data(
    file_path: str,
    target_column: str
):

    df = pd.read_csv(file_path)

    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in dataset")

    X = df.drop(columns=[target_column])
    y = df[target_column]

    return X, y
