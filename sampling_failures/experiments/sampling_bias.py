import pandas as pd
import numpy as np

np.random.seed(42)
N = 10000

RESULTS_PATH = "sampling_failures/results/sampling_bias.csv"

population = pd.DataFrame({
    "income": np.random.normal(60000, 15000, N).clip(20000, 150000),
    "credit_score": np.random.normal(650, 70, N).clip(300, 850)
})

population["default_prob"] = (
    0.4 * (population["credit_score"] < 600).astype(int) +
    0.3 * (population["income"] < 40000).astype(int)
)

population["default"] = np.random.binomial(1, population["default_prob"])

true_default_rate = population["default"].mean()

approved_only = population[
    (population["credit_score"] >= 620) &
    (population["income"] >= 45000)
]

biased_default_rate = approved_only["default"].mean()

summary = pd.DataFrame({
    "dataset": ["population", "approved_only"],
    "rows": [len(population), len(approved_only)],
    "default_rate": [true_default_rate, biased_default_rate],
    "avg_income": [
        population["income"].mean(),
        approved_only["income"].mean()
    ],
    "avg_credit_score": [
        population["credit_score"].mean(),
        approved_only["credit_score"].mean()
    ]
})

summary.to_csv(RESULTS_PATH, index=False)

