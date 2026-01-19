import pandas as pd
import re

DATETIME_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MIN_ROWS_FOR_IDENTIFIER = 20

def analyze_feature_inference(rows: list[dict]) -> dict:

    df = pd.DataFrame(rows)

    if df.empty:
        raise ValueError("Empty dataset")

    total_rows = len(df)
    result = {}

    for col in df.columns:
        series = df[col].dropna()

        if series.empty:
            result[col] = {
                "inferred_type": "unknown",
                "confidence": 0.0,
                "warnings": ["all values missing"]
            }
            continue

        unique_ratio = series.nunique() / len(series)

        #Binary
        if set(series.unique()).issubset({0, 1, True, False}):
            result[col] = {
                "inferred_type": "binary",
                "confidence": 0.95,
                "warnings": []
            }
            continue

    #Numeric
        if pd.api.types.is_numeric_dtype(series):
            if total_rows >= MIN_ROWS_FOR_IDENTIFIER and unique_ratio > 0.9:
                result[col] = {
                    "inferred_type": "identifier",
                    "confidence": 0.85,
                    "warnings": ["high cardinality numeric column"]
                }
            else:
                result[col] = {
                    "inferred_type": "numerical",
                    "confidence": 0.9,
                    "warnings": []
                }
            continue

    #Datetime
        if(
            series.dtype == object
            and series.astype(str).str.fullmatch(DATETIME_REGEX).all()
            ):
            result[col] = {
                "inferred_type": "datetime",
                "confidence": 0.95,
                "warnings": ["string encoded datetime"]
            }
            continue

        #Categorical or text
        if series.dtype == object:
            if unique_ratio < 0.3:
                inferred = "categorical"
                confidence = 0.85
            else:
                inferred = "text"
                confidence = 0.8

            result[col] = {
                "inferred_type": inferred,
                "confidence": confidence,
                "warnings": []
            }
            continue

    #default
        result[col] = {
            "inferred_type": "unknown",
            "confidence": 0.5,
            "warnings": ["unrecognized pattern"]
        }

    return {"columns": result}
# {
#   "data": [
#     {
#       "age": 25,
#       "user_id": 1001,
#       "city": "NY",
#       "active": 1,
#       "created_at": "2024-01-01",
#       "comment": "good service"
#     },
#     {
#       "age": 30,
#       "user_id": 1002,
#       "city": "SF",
#       "active": 0,
#       "created_at": "2024-01-02",
#       "comment": "bad experience"
#     }
#   ]
# }

