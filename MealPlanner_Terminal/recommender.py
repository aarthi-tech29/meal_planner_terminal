import pandas as pd

df = pd.read_csv("cleaned_foods.csv")


def recommend_meals(
    goal,
    diet_type,
    health_condition
):

    foods = df.copy()

    if diet_type:

        foods = foods[
            foods["Diet_Type"]
            .str.lower()
            ==
            diet_type.lower()
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
        ]

        meal_plan[category] = (
            items["Food"]
            .head(3)
            .tolist()
        )

    return meal_plan