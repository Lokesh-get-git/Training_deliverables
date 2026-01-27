# ml_pipeline/data/split_data.py

from sklearn.model_selection import train_test_split


def split_train_test(
    X,
    y,
    test_size: float = 0.2,
    random_state: int = 42,
    stratify: bool = False
):

    stratify_y = y if stratify else None

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=stratify_y
    )

    return X_train, X_test, y_train, y_test
