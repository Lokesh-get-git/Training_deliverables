import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

np.random.seed(42)
N = 5000

RESULTS_PATH = "sampling_failures/results/leakage_metrics.txt"

X = pd.DataFrame({
    "income": np.random.normal(60000, 15000, N),
    "credit_score": np.random.normal(650, 70, N)
})

# True target
y = ((X["credit_score"] < 600) | (X["income"] < 40000)).astype(int)

X["leaked_feature"] = y

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

with open(RESULTS_PATH, "w") as f:
    f.write("DATA LEAKAGE EXPERIMENT RESULTS\n\n")
    f.write("Model trained WITH leaked feature\n\n")
    f.write(f"Accuracy: {accuracy:.2%}\n\n")
    f.write("Confusion Matrix:\n")
    f.write(str(cm))

