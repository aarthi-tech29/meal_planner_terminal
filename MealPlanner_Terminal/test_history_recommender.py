from history_recommender import (
    get_user_preferences
)

user = input(
    "Enter Username: "
)

preferences = get_user_preferences(
    user
)

if preferences:

    print(
        "\n===== USER PREFERENCES ====="
    )

    for meal, food in preferences.items():

        print(
            meal,
            "→",
            food
        )

else:

    print(
        "No history found."
    )