import pandas as pd

def get_user_preferences(username):

    try:
        df = pd.read_csv("history.csv")

        # Check required columns
        required_columns = [
            "Name",
            "Breakfast",
            "Lunch",
            "Dinner",
            "Snack"
        ]

        for col in required_columns:
            if col not in df.columns:
                print(f"Column missing: {col}")
                return None

        # Filter user
        user_data = df[
            df["Name"].astype(str).str.lower()
            ==
            username.lower()
        ]

        if user_data.empty:
            return None

        preferences = {}

        for meal in [
            "Breakfast",
            "Lunch",
            "Dinner",
            "Snack"
        ]:

            # Remove empty values
            values = user_data[meal].dropna()

            if len(values) == 0:
                preferences[meal] = "No Data"
            else:
                preferences[meal] = values.mode().iloc[0]

        return preferences

    except Exception as e:
        print("History Error:", e)
        return None