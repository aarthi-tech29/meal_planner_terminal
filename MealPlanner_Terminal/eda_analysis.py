import pandas as pd

df = pd.read_csv("cleaned_foods.csv")

print("\n========== DATASET INFO ==========")

print(df.head())

print("\n========== CATEGORY COUNTS ==========")

print(df["Category"].value_counts())

print("\n========== AVERAGE CALORIES ==========")

print(df["Calories"].mean())

print("\n========== HIGHEST CALORIE FOOD ==========")

print(
    df.loc[
        df["Calories"].idxmax()
    ]
)