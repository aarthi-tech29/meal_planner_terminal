import pandas as pd

df = pd.read_csv("foods.csv")

print("Original Records:", len(df))



# Remove missing values
df["Health_Condition"] = df[
    "Health_Condition"
].fillna("None")

# Remove duplicates
df = df.drop_duplicates()

print("Cleaned Records:", len(df))

df.to_csv(
    "cleaned_foods.csv",
    index=False
)

print("Dataset cleaned successfully")