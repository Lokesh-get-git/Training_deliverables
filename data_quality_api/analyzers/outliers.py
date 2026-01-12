import pandas as pd

def analyze_outliers(rows: list[dict]) -> dict:
    df = pd.DataFrame(rows)

    if df.empty:
        raise ValueError("Empty dataset")

    return {}
# {
#   "data": [
#     { "income": 50000 },
#     { "income": 52000 },
#     { "income": 51000 },
#     { "income": 48000 },
#     { "income": 1000000 }
#   ]
# }
