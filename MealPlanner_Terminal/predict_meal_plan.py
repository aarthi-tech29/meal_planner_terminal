import pandas as pd
import joblib

print("\n========== ML MEAL PLAN PREDICTION ==========\n")

goal = input(
    "Enter Goal (Weight Loss/Weight Gain/Maintenance): "
)

bmi = float(
    input(
        "Enter BMI: "
    )
)
diet = input(
    "Enter Diet Type: "
)

health = input(
    "Enter Health Condition: "
)

# Load Goal Encoder
goal_encoder = joblib.load(
    "goal_encoder.pkl"
)
diet_encoder = joblib.load(
    "diet_encoder.pkl"
)

health_encoder = joblib.load(
    "health_encoder.pkl"
)

goal_encoded = goal_encoder.transform(
    [goal]
)[0]
diet_encoded = diet_encoder.transform(
    [diet]
)[0]

health_encoded = health_encoder.transform(
    [health]
)[0]

# Create Input Data
data = pd.DataFrame(
    {
        "Goal":[goal_encoded],
        "BMI":[bmi],
        "Diet_Type":[diet_encoded],
        "Health_Condition":[health_encoded]
    }
)

# =========================
# BREAKFAST
# =========================

breakfast_model = joblib.load(
    "breakfast_model.pkl"
)

breakfast_encoder = joblib.load(
    "breakfast_encoder.pkl"
)

breakfast_prediction = (
    breakfast_model.predict(data)
)

breakfast = (
    breakfast_encoder.inverse_transform(
        breakfast_prediction
    )[0]
)

# =========================
# LUNCH
# =========================

lunch_model = joblib.load(
    "lunch_model.pkl"
)

lunch_encoder = joblib.load(
    "lunch_encoder.pkl"
)

lunch_prediction = (
    lunch_model.predict(data)
)

lunch = (
    lunch_encoder.inverse_transform(
        lunch_prediction
    )[0]
)

# =========================
# DINNER
# =========================

dinner_model = joblib.load(
    "dinner_model.pkl"
)

dinner_encoder = joblib.load(
    "dinner_encoder.pkl"
)

dinner_prediction = (
    dinner_model.predict(data)
)

dinner = (
    dinner_encoder.inverse_transform(
        dinner_prediction
    )[0]
)

# =========================
# SNACK
# =========================

snack_model = joblib.load(
    "snack_model.pkl"
)

snack_encoder = joblib.load(
    "snack_encoder.pkl"
)

snack_prediction = (
    snack_model.predict(data)
)

snack = (
    snack_encoder.inverse_transform(
        snack_prediction
    )[0]
)

# =========================
# DISPLAY RESULT
# =========================

print("\n===================================")
print(" PERSONALIZED ML MEAL PLAN")
print("===================================\n")

print("🥣 Breakfast :", breakfast)

print("🍛 Lunch     :", lunch)

print("🍲 Dinner    :", dinner)

print("🍎 Snack     :", snack)

print("\n===================================")
print("Generated using History-Based")
print("Machine Learning Models")
print("===================================")