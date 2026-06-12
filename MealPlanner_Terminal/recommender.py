import pandas as pd

df = pd.read_csv("foods.csv")


def recommend_meals(
    goal,
    diet_type,
    health_condition
):

    foods = df.copy()

    # ==========================
    # Diet Filter
    # ==========================

    if diet_type:

        foods = foods[
            foods["Diet_Type"]
            .str.lower()
            ==
            diet_type.lower()
        ]

    # ==========================
    # Health Filter
    # ==========================

    if health_condition.lower() == "none":

        foods = foods[
            foods["Health_Condition"]
            .fillna("None")
            .str.lower()
            ==
            "none"
        ]

    else:

        foods = foods[
            foods["Health_Condition"]
            .fillna("")
            .str.lower()
            ==
            health_condition.lower()
        ]

    meal_plan = {}

    for category in [
        "Breakfast",
        "Lunch",
        "Dinner",
        "Snack"
    ]:

        items = foods[
            foods["Category"]
            ==
            category
        ].copy()

        # Goal-wise filtering

        if goal.lower() == "weight loss":

            items = items[
                items["Calories"] <= 300
            ]

        elif goal.lower() == "weight gain":

            items = items[
                items["Calories"] >= 200
            ]

        elif goal.lower() == "maintenance":

            items = items[
                (items["Calories"] >= 100)
                &
                (items["Calories"] <= 400)
            ]

        # If no items found use category foods

        if len(items) == 0:

            items = foods[
                foods["Category"]
                ==
                category
            ]

        meal_plan[category] = (
            items["Food"]
            .drop_duplicates()
            .head(3)
            .tolist()
        )

    return meal_plan