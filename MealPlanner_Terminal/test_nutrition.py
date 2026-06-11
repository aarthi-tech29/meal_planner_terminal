from recommender import recommend_meals
from nutrition import nutrition_totals

meal_plan = recommend_meals(
    "Weight Loss",
    "Vegetarian",
    "None"
)

nutrition = nutrition_totals(
    meal_plan
)

print("\n====== NUTRITION REPORT ======")

print(
    "Calories:",
    nutrition["calories"]
)

print(
    "Protein:",
    nutrition["protein"],
    "g"
)

print(
    "Carbs:",
    nutrition["carbs"],
    "g"
)

print(
    "Fat:",
    nutrition["fat"],
    "g"
)