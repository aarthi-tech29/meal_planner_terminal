import pandas as pd
import random

records = []

# ==========================
# WEIGHT LOSS USERS
# ==========================

for _ in range(80):

    health = random.choice([
        "None",
        "Diabetes",
        "Heart Disease"
    ])

    records.append([
        "Advika",
        "Weight Loss",
        round(random.uniform(20.0, 23.0), 1),

        random.choice([
            "Vegetarian",
            "Vegan",
            "Non-Vegetarian"
        ]),

        health,

        random.choice([
            "Oats",
            "Diabetic Oats",
            "Idli",
            "Dosa"
        ]),

        random.choice([
            "Paneer Curry",
            "Diabetic Salad",
            "Chapati"
        ]),

        random.choice([
            "Khichdi",
            "Diabetic Soup",
            "Paneer Bhurji"
        ]),

        random.choice([
            "Yogurt",
            "Diabetic Snack",
            "Milk"
        ])
    ])

# ==========================
# WEIGHT GAIN USERS
# ==========================

for _ in range(60):

    records.append([
        "Riya",
        "Weight Gain",
        round(random.uniform(18.0, 20.0), 1),

        random.choice([
            "Vegetarian",
            "Vegan",
            "Non-Vegetarian"
        ]),

        "None",   # Health Condition

        random.choice([
            "Muesli",
            "Weight Gain Shake",
            "Peanut Butter Toast"
        ]),

        random.choice([
            "Weight Gain Rice",
            "Vegetable Pulao"
        ]),

        random.choice([
            "Paneer Tikka",
            "Paneer Curry"
        ]),

        random.choice([
            "Protein Shake",
            "Paneer Roll"
        ])
    ])

# ==========================
# MAINTENANCE USERS
# ==========================

for _ in range(60):

    records.append([
        "John",
        "Maintenance",
        round(random.uniform(23.0, 25.0), 1),

        random.choice([
            "Vegetarian",
            "Vegan",
            "Non-Vegetarian"
        ]),

        "None",

        random.choice([
            "Dosa",
            "Idli",
            "Upma"
        ]),

        random.choice([
            "Brown Rice",
            "Quinoa"
        ]),

        random.choice([
            "Vegetable Soup",
            "Tomato Soup"
        ]),

        random.choice([
            "Apple",
            "Banana"
        ])
    ])

# ==========================
# CREATE DATAFRAME
# ==========================

df = pd.DataFrame(
    records,
    columns=[
        "Name",
        "Goal",
        "BMI",
        "Diet_Type",
        "Health_Condition",
        "Breakfast",
        "Lunch",
        "Dinner",
        "Snack"
    ]
)

# ==========================
# SAVE CSV
# ==========================

df.to_csv(
    "history.csv",
    index=False
)

print("\nHistory Dataset Generated Successfully")
print("Total Records:", len(df))

print("\nDiet Types:")
print(df["Diet_Type"].value_counts())

print("\nHealth Conditions:")
print(df["Health_Condition"].value_counts())