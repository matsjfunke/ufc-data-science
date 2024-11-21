"""
matsjfunke
"""

from datetime import datetime

import pandas as pd
from skimpy import skim

from general_importance_plot import general_feature_importance
from height_reach_plot import height_reach_plot

# Read CSV
df = pd.read_csv("./ufc-fighters-statistics.csv", sep=",", index_col=0)

# remove nickname column & rows containing NA
df = df.drop(columns="nickname")
df = df.dropna()

# Dataframe overview
print(df.head())
print(f"Dataframe has {df.shape[1]} columns and {df.shape[0]} rows")

# renamed columns
df = df.rename(
    columns={
        "average_takedowns_landed_per_15_minutes": "takedowns_landed_per_15_minutes",
        "average_submissions_attempted_per_15_minutes": "submissions_attempted_per_15_minutes",
    }
)

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
def assign_weight_class(weight, bins, labels):
    for i in range(len(bins) - 1):
        if bins[i] <= weight < bins[i + 1]:
            return labels[i]
    return None


bins = [52.5, 56.7, 61.2, 65.8, 70.3, 77.1, 83.9, 93.0, 120.2, float("inf")]
labels = ["straw", "fly", "bantam", "feather", "light", "welter", "middle", "light-heavy", "heavy"]
df["weight_class"] = df["weight_in_kg"].apply(lambda w: assign_weight_class(w, bins, labels)).astype("category")

# Convert the 'stance' column to category data type
df["stance"] = df["stance"].astype("category")

# view cleaned data
skim(df)

# analize and plot height & reach
height_reach_plot(df, save=True, show=False)

features = [
    "submissions_attempted_per_15_minutes",
    "takedowns_landed_per_15_minutes",
    "significant_strikes_landed_per_minute",
    "height_cm",
    "reach_in_cm",
    "takedown_defense",
    "takedown_accuracy",
    "significant_strike_defence",
    "significant_striking_accuracy",
]

general_feature_importance(df, features, save=True, show=True)
