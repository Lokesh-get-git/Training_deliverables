import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)

num_samples = 100

study_time = np.random.uniform(20, 80, num_samples)
noise = np.random.normal(0, 15, num_samples)
score = 1.5 * study_time + 20 + noise


score = np.maximum(0, score)
df=pd.DataFrame({
    "study_time":study_time,
    "score":score
})

df.to_csv("ml_from_scratch\synthetic_data\linear_regression_data.csv", index=False)

plt.scatter(df.study_time,df.score)
# plt.scatter(df_linear.num_rooms,df_linear.distance_city)
# plt.scatter(df_linear.num_rooms,df_linear.distance_city)
plt.show()
print("Saved linear_regression_data.csv")
print(df.head())
print(df.describe())
