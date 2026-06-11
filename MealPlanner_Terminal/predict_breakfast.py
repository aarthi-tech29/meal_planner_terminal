import joblib
import pandas as pd

# Load saved model
model = joblib.load(
    "breakfast_model.pkl"
)

goal_encoder = joblib.load(
    "goal_encoder.pkl"
)

breakfast_encoder = joblib.load(
    "breakfast_encoder.pkl"
)

print("\n===== BREAKFAST PREDICTION =====\n")

goal = input(
    "Enter Goal (Weight Loss/Weight Gain/Maintenance): "
)

bmi = float(
    input("Enter BMI: ")
)

# Encode goal
goal_encoded = goal_encoder.transform(
    [goal]
)[0]

# Create dataframe
data = pd.DataFrame(
    {
        "Goal":[goal_encoded],
        "BMI":[bmi]
    }
)

# Predict
prediction = model.predict(data)

# Decode prediction
breakfast = breakfast_encoder.inverse_transform(
    prediction
)[0]

print(
    "\nRecommended Breakfast:",
    breakfast
)