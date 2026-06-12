from calorie import (
    calculate_bmi,
    bmi_category,
    calculate_bmr,
    calculate_tdee,
    calorie_goal
)

from recommender import recommend_meals
from nutrition import nutrition_totals
from history_recommender import (
    get_user_preferences
)
import joblib
import pandas as pd

from history_recommender import (
    get_user_preferences
)

print("\n===================================")
print("     MEAL PLANNER APPLICATION")
print("===================================\n")

# User Input

name = input("Enter Name: ")

age = int(
    input("Enter Age: ")
)

gender = input(
    "Enter Gender (Male/Female): "
)

height = float(
    input("Enter Height (cm): ")
)

weight = float(
    input("Enter Weight (kg): ")
)

activity = input(
    "Enter Activity Level (sedentary/light/moderate/active): "
)

goal = input(
    "Enter Goal (Weight Loss/Weight Gain/Maintenance): "
)

diet = input(
    "Enter Diet Type (Vegetarian/Vegan/Non-Vegetarian): "
)

health = input(
    "Enter Health Condition (None/Diabetes/Heart Disease): "
)

# BMI

bmi = calculate_bmi(
    weight,
    height
)

# =========================
# ML Meal Prediction
# =========================

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

data = pd.DataFrame(
    {
        "Goal": [goal_encoded],
        "BMI": [bmi],
        "Diet_Type": [diet_encoded],
        "Health_Condition": [health_encoded]
    }
)

# Breakfast
breakfast_model = joblib.load(
    "breakfast_model.pkl"
)

breakfast_encoder = joblib.load(
    "breakfast_encoder.pkl"
)

ml_breakfast = (
    breakfast_encoder.inverse_transform(
        breakfast_model.predict(data)
    )[0]
)

# Lunch
lunch_model = joblib.load(
    "lunch_model.pkl"
)

lunch_encoder = joblib.load(
    "lunch_encoder.pkl"
)

ml_lunch = (
    lunch_encoder.inverse_transform(
        lunch_model.predict(data)
    )[0]
)

# Dinner
dinner_model = joblib.load(
    "dinner_model.pkl"
)

dinner_encoder = joblib.load(
    "dinner_encoder.pkl"
)

ml_dinner = (
    dinner_encoder.inverse_transform(
        dinner_model.predict(data)
    )[0]
)

# Snack
snack_model = joblib.load(
    "snack_model.pkl"
)

snack_encoder = joblib.load(
    "snack_encoder.pkl"
)

ml_snack = (
    snack_encoder.inverse_transform(
        snack_model.predict(data)
    )[0]
)

status = bmi_category(
    bmi
)

# BMR

bmr = calculate_bmr(
    weight,
    height,
    age,
    gender
)

# TDEE

tdee = calculate_tdee(
    bmr,
    activity
)

# Target Calories

target = calorie_goal(
    tdee,
    goal
)

# Meal Recommendation

meal_plan = recommend_meals(
    goal,
    diet,
    health
)
preferences = get_user_preferences(
    name,
    goal,
    diet,
    health
)
print("\nDEBUG INPUTS")
print("Name:", repr(name))
print("Goal:", repr(goal))
print("Diet:", repr(diet))
print("Health:", repr(health))
# Nutrition Analysis

nutrition = nutrition_totals(
    meal_plan
)

# Display Results

print("\n===================================")
print("          USER SUMMARY")
print("===================================\n")

print("Name:", name)

print("BMI:", bmi)

print("BMI Status:", status)

print("BMR:", round(bmr))

print("TDEE:", round(tdee))

print("Target Calories:", target)

print("\n===================================")
print("      RECOMMENDED MEAL PLAN")
print("===================================")

for meal, foods in meal_plan.items():

    print(f"\n{meal}")

    for food in foods:

        print("-", food)

print("\n===================================")
print("      NUTRITION ANALYSIS")
print("===================================\n")

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
print("\n===================================")
print(" HISTORY-BASED RECOMMENDATION")
print("===================================\n")

if preferences:

    print(
        "Based on previous meal selections:"
    )

    for meal, food in preferences.items():

        print(
            f"{meal}: ⭐ {food}"
        )

else:

    print(
        "No previous history found."
    )
print("\n===================================")
print(" ML PREDICTED MEAL PLAN")
print("===================================\n")

print(
    "Breakfast: ⭐",
    ml_breakfast
)

print(
    "Lunch: ⭐",
    ml_lunch
)

print(
    "Dinner: ⭐",
    ml_dinner
)

print(
    "Snack: ⭐",
    ml_snack
)
print("\n===================================")
print("     MACHINE LEARNING MODEL")
print("===================================\n")

print(
    "Model: Random Forest Classifier"
)

print(
    "Accuracy: 50%"
)

print("\nThank you for using Meal Planner!")

# input
# 1. Weight Loss + Diabetes (Vegetarian)
# Name: Advika
# Age: 25
# Gender: Female
# Height: 160
# Weight: 70
# Activity Level: light
# Goal: Weight Loss
# Diet Type: Vegetarian
# Health Condition: Diabetes

# 2. Weight Loss + Heart Disease (Vegetarian)
# Name: Priya
# Age: 50
# Gender: Female
# Height: 168
# Weight: 78
# Activity Level: light
# Goal: Weight Loss
# Diet Type: Vegetarian
# Health Condition: Heart Disease

# 3. Weight Loss + Heart Disease (Non-Vegetarian)
# Name: Advika
# Age: 40
# Gender: Female
# Height: 160
# Weight: 80
# Activity Level: light
# Goal: Weight Loss
# Diet Type: Non-Vegetarian
# Health Condition: Heart Disease

# 4. Weight Gain (Vegetarian)
# Name: Riya
# Age: 22
# Gender: Female
# Height: 165
# Weight: 50
# Activity Level: active
# Goal: Weight Gain
# Diet Type: Vegetarian
# Health Condition: None

# 5. Maintenance (Vegan)
# Name: Arun
# Age: 30
# Gender: Male
# Height: 170
# Weight: 85
# Activity Level: moderate
# Goal: Maintenance
# Diet Type: Vegan
# Health Condition: None

# 6. Maintenance (Non-Vegetarian)
# Name: David
# Age: 30
# Gender: Male
# Height: 175
# Weight: 74
# Activity Level: light
# Goal: Maintenance
# Diet Type: Non-Vegetarian
# Health Condition: None