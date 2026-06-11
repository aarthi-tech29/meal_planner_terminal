import pandas as pd

df = pd.read_csv("history.csv")

print("\n========== USER BEHAVIOR ANALYSIS ==========\n")

print("Total Records:")
print(len(df))

print("\nMost Common Goal:")

print(
    df["Goal"].value_counts()
)

print("\nAverage BMI:")

print(
    round(
        df["BMI"].mean(),
        2
    )
)

print("\nMost Preferred Breakfast:")

print(
    df["Breakfast"]
    .value_counts()
    .head(5)
)

print("\nMost Preferred Lunch:")

print(
    df["Lunch"]
    .value_counts()
    .head(5)
)

print("\nMost Preferred Dinner:")

print(
    df["Dinner"]
    .value_counts()
    .head(5)
)

print("\nMost Preferred Snack:")

print(
    df["Snack"]
    .value_counts()
    .head(5)
)