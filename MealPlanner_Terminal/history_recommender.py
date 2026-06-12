import pandas as pd

def get_user_preferences(
    username,
    goal,
    diet_type,
    health_condition
):

    try:

        df = pd.read_csv(
            "history.csv",
            keep_default_na=False
        )

        # Convert everything to lowercase strings
        for col in [
            "Name",
            "Goal",
            "Diet_Type",
            "Health_Condition"
        ]:
            df[col] = (
                df[col]
                .fillna("")
                .astype(str)
                .str.strip()
                .str.lower()
            )

        username = username.strip().lower()
        goal = goal.strip().lower()
        diet_type = diet_type.strip().lower()
        health_condition = health_condition.strip().lower()

        user_data = df[
            (df["Name"].astype(str).str.strip().str.lower()
                == username.strip().lower())
            &
            (df["Goal"].astype(str).str.strip().str.lower()
                == goal.strip().lower())
            &
            (df["Diet_Type"].astype(str).str.strip().str.lower()
                == diet_type.strip().lower())
            &
            (df["Health_Condition"].astype(str).str.strip().str.lower()
                == health_condition.strip().lower())
        ]

        # print("\nDEBUG MATCHES:")
        # print(user_data)
        # print("Rows Found:", len(user_data))

        if user_data.empty:
            return None

        preferences = {}

        for meal in [
            "Breakfast",
            "Lunch",
            "Dinner",
            "Snack"
        ]:

            mode_values = user_data[meal].mode()

            if len(mode_values) > 0:
                preferences[meal] = mode_values.iloc[0]
            else:
                preferences[meal] = "No Data"

        return preferences

    except Exception as e:

        print("History Error:", e)
        return None