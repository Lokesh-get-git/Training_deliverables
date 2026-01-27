import pandas as pd
import numpy as np


def classification_error_analysis(X_test, y_true, y_pred):
    errors = X_test.copy()
    errors["y_true"] = y_true
    errors["y_pred"] = y_pred
    errors["is_error"] = errors["y_true"] != errors["y_pred"]

    return errors[errors["is_error"]]


def regression_error_analysis(X_test, y_true, y_pred):
    errors = X_test.copy()
    errors["y_true"] = y_true
    errors["y_pred"] = y_pred
    errors["residual"] = y_true - y_pred
    errors["abs_residual"] = np.abs(errors["residual"])

    return errors.sort_values("abs_residual", ascending=False)
