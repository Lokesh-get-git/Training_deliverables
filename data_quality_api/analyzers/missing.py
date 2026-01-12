import pandas as pd

def analyze_missing(rows: list[dict]) -> dict:
    df = pd.DataFrame(rows)

    total_rows = len(df)
    total_columns = len(df.columns)
    missing_counts = df.isna().sum()
    missing_percentages = (missing_counts / total_rows * 100).round(2)

    columns = {
        col: {
            "missing_count": int(missing_counts[col]),
            "missing_percentage": float(missing_percentages[col])
        }
        for col in df.columns
    }

    row_missing_counts = df.isna().sum(axis=1).tolist()

    return {
        "total_rows": total_rows,
        "total_columns": total_columns,
        "columns": columns,
        "row_missing_counts": row_missing_counts
    }
# {
#   "data": [
#     { "age": 25, "income": 50000 },
#     { "age": null, "income": 60000 },
#     { "age": 30, "income": null }
#   ]
# }
