"""
matsjfunke
"""

from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
from skimpy import skim

# Read CSV
df = pd.read_csv("./ufc-fighters-statistics.csv", sep=",", index_col=0)

# remove nickname column & rows containing NA
df = df.drop(columns="nickname")
df = df.dropna()

# Dataframe overview
print(df.head())
print(f"Dataframe has {df.shape[1]} columns and {df.shape[0]} rows")

# ensure 'date_of_birth' is in datetime format
df["date_of_birth"] = pd.to_datetime(df["date_of_birth"])

# calculate & add age column
current_date = datetime.now()
df["age"] = (
    current_date.year
    - df["date_of_birth"].dt.year
    - (
        (current_date.month < df["date_of_birth"].dt.month)
        | ((current_date.month == df["date_of_birth"].dt.month) & (current_date.day < df["date_of_birth"].dt.day))
    )
)

# calculate & add  total_fights & win_percentage columns
df["total_fights"] = df["wins"] + df["losses"] + df["draws"]
df["win_percentage"] = round((df["wins"] / df["total_fights"]) * 100, 2)


# Assign weight classes
bins = [52.5, 56.7, 61.2, 65.8, 70.3, 77.1, 83.9, 102.1, 120.2, float("inf")]
labels = ["straw", "fly", "bantam", "feather", "light", "welter", "middle", "light-heavy", "heavy"]
df["weight_class"] = pd.cut(df["weight_in_kg"], bins=bins, labels=labels, right=True)

# Convert the 'stance' column to category data type
df["stance"] = df["stance"].astype("category")

# view cleaned data
skim(df)
