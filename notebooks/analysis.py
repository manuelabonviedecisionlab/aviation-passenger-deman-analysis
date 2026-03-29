import pandas as pd

df = pd.read_csv("aviation_data.csv")

print(df.head())
print(df.describe())

# Simple analysis
total_passengers = df["passengers"].sum()
print("Total passengers:", total_passengers)
