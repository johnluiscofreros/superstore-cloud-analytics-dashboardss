import pandas as pd

# Load original dataset
df = pd.read_csv("train.csv")

# Select only 800 rows
df_sample = df.sample(n=800, random_state=42)

# Save the smaller dataset
df_sample.to_csv("superstore_800_rows.csv", index=False)

print("Dataset successfully reduced!")
print("Rows:", len(df_sample))