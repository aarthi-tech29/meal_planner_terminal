import pandas as pd

df = pd.read_csv("cleaned_foods.csv")


def nutrition_totals(meal_plan):

    calories = 0
    protein = 0
    carbs = 0
    fat = 0

    for foods in meal_plan.values():

        for food in foods:

            row = df[
                df["Food"] == food
            ]

            if not row.empty:

                calories += row[
                    "Calories"
                ].values[0]

                protein += row[
                    "Protein"
                ].values[0]

                carbs += row[
                    "Carbs"
                ].values[0]

                fat += row[
                    "Fat"
                ].values[0]

    return {
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fat": fat
    }