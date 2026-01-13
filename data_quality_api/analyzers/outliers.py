import pandas as pd

def analyze_outliers(rows: list[dict]) -> dict:
    df = pd.DataFrame(rows)

    if df.empty:
        raise ValueError("Empty dataset")

    numeric_df = df.select_dtypes(include=["number"])

    result = {}

    total_rows = len(df)

    for col in numeric_df.columns:
        series = numeric_df[col].dropna()

        if series.empty:
            continue

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1

        if iqr == 0:
            continue  

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = series[
            (series < lower_bound) | (series > upper_bound)
        ]

        if outliers.empty:
            continue

        result[col] = {
            "outlier_count": int(len(outliers)),
            "outlier_percentage": round(len(outliers) / total_rows * 100, 2),
            "lower_bound": float(lower_bound),
            "upper_bound": float(upper_bound)
        }

    return {
        "method": "iqr",
        "columns": result
    }

# {
#   "data": [
#     { "income": 50000 },
#     { "income": 52000 },
#     { "income": 51000 },
#     { "income": 48000 },
#     { "income": 1000000 }
#   ]
# }
