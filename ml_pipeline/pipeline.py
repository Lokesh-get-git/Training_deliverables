from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from .evaluation.validate import validate_model
from .evaluation.error_analysis import (
    classification_error_analysis,
    regression_error_analysis
)


def build_pipeline(model, numerical_cols, categorical_cols):
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ]
    )

    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    return pipeline


def run_pipeline(
    X_train,
    X_test,
    y_train,
    y_test,
    model,
    numerical_cols,
    categorical_cols,
    task_type
):

    pipeline = build_pipeline(
        model=model,
        numerical_cols=numerical_cols,
        categorical_cols=categorical_cols
    )

    pipeline.fit(X_train, y_train)

    y_train_pred = pipeline.predict(X_train)     
    y_test_pred = pipeline.predict(X_test)

    metrics = validate_model(
        y_train,
        y_train_pred,
        y_test,
        y_test_pred,
        task_type=task_type
    )

    if task_type == "classification":
        errors = classification_error_analysis(
            X_test, y_test, y_test_pred
        )
    else:
        errors = regression_error_analysis(
            X_test, y_test, y_test_pred
        )

    return metrics, errors
