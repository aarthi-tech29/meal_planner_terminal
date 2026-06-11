from recommender import recommend_meals

plan = recommend_meals(
    "Weight Loss",
    "Vegetarian",
    "None"
)

for meal, foods in plan.items():

    print("\n", meal)

    for food in foods:

        print("-", food)