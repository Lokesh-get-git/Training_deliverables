from .metrics import classification_metrics, regression_metrics


def validate_model(
    y_train,
    y_train_pred,
    y_test,
    y_test_pred,
    task_type: str
):

    if task_type == "classification":
        train_metrics = classification_metrics(y_train, y_train_pred)
        test_metrics = classification_metrics(y_test, y_test_pred)

    elif task_type == "regression":
        train_metrics = regression_metrics(y_train, y_train_pred)
        test_metrics = regression_metrics(y_test, y_test_pred)

    else:
        raise ValueError("task_type must be 'classification' or 'regression'")

    return {
        "train": train_metrics,
        "test": test_metrics
    }
