import numpy as np
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix

np.random.seed(42)
N = 10000
MINORITY_RATE = 0.05  # 5% positive class

RESULTS_PATH = "sampling_failures/results/class_imbalance_metrics.txt"

y_true = np.array([1] * int(N * MINORITY_RATE) + [0] * int(N * (1 - MINORITY_RATE)))
np.random.shuffle(y_true)

y_pred = np.zeros_like(y_true)

accuracy = accuracy_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
cm = confusion_matrix(y_true, y_pred)

with open(RESULTS_PATH, "w") as f:
    f.write("CLASS IMBALANCE EXPERIMENT RESULTS\n\n")
    f.write(f"Total samples: {N}\n")
    f.write(f"Minority class rate: {MINORITY_RATE * 100:.2f}%\n\n")
    f.write(f"Accuracy: {accuracy:.2%}\n")
    f.write(f"Recall (minority class): {recall:.2%}\n\n")
    f.write("Confusion Matrix:\n")
    f.write(str(cm))

