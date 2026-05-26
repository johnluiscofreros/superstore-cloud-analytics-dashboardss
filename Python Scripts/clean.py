import pandas as pd

df = pd.read_csv("superstore_800_rows.csv")

df = df.dropna()

df["sales_norm"] = (df["Sales"] - df["Sales"].min()) / (df["Sales"].max() - df["Sales"].min())

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1

df = df[(df["Sales"] >= Q1 - 1.5*IQR) & (df["Sales"] <= Q3 + 1.5*IQR)]

df.to_csv("cleaned_superstore.csv", index=False)

print("DONE CLEANING")