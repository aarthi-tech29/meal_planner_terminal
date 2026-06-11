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
    name
)
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
# Enter Name: Advika
# Enter Age: 15
# Enter Gender (Male/Female): Female
# Enter Height (cm): 160
# Enter Weight (kg): 70
# Enter Activity Level (sedentary/light/moderate/active): light
# Enter Goal (Weight Loss/Weight Gain/Maintenance): Weight Loss
# Enter Diet Type (Vegetarian/Vegan/Non-Vegetarian): Non-Vegetarian
# Enter Health Condition (None/Diabetes/Heart Disease): None

# Name: John
# Age: 28
# Gender: Male
# Height: 175
# Weight: 74
# Activity: light
# Goal: Maintenance

# Enter Name: Riya
# Enter Age: 50
# Enter Gender (Male/Female): Female
# Enter Height (cm): 160
# Enter Weight (kg): 80
# Enter Activity Level (sedentary/light/moderate/active): sedentary
# Enter Goal (Weight Loss/Weight Gain/Maintenance): Weight Gain
# Enter Diet Type (Vegetarian/Vegan/Non-Vegetarian): Vegan
# Enter Health Condition (None/Diabetes/Heart Disease): Diabetes50
# ==============================
# Input 1 – Weight Loss + Diabetes
# Enter Name: Advika
# Enter Age: 25
# Enter Gender (Male/Female): Female
# Enter Height (cm): 160
# Enter Weight (kg): 70
# Enter Activity Level (sedentary/light/moderate/active): light
# Enter Goal (Weight Loss/Weight Gain/Maintenance): Weight Loss
# Enter Diet Type (Vegetarian/Vegan/Non-Vegetarian): Vegetarian
# Enter Health Condition (None/Diabetes/Heart Disease): Diabetes

# Expected ML output:

# Breakfast: Diabetic Oats
# Lunch: Diabetic Salad
# Dinner: Diabetic Soup
# Snack: Diabetic Snack
# Input 2 – Weight Gain
# Enter Name: Riya
# Enter Age: 22
# Enter Gender (Male/Female): Female
# Enter Height (cm): 165
# Enter Weight (kg): 50
# Enter Activity Level (sedentary/light/moderate/active): active
# Enter Goal (Weight Loss/Weight Gain/Maintenance): Weight Gain
# Enter Diet Type (Vegetarian/Vegan/Non-Vegetarian): Vegetarian
# Enter Health Condition (None/Diabetes/Heart Disease): None

# Expected ML output:

# Breakfast: Muesli
# Lunch: Weight Gain Rice
# Dinner: Paneer Tikka
# Snack: Protein Shake
# Input 3 – Maintenance
# Enter Name: John
# Enter Age: 30
# Enter Gender (Male/Female): Male
# Enter Height (cm): 175
# Enter Weight (kg): 74
# Enter Activity Level (sedentary/light/moderate/active): light
# Enter Goal (Weight Loss/Weight Gain/Maintenance): Maintenance
# Enter Diet Type (Vegetarian/Vegan/Non-Vegetarian): Vegan
# Enter Health Condition (None/Diabetes/Heart Disease): None

# Expected ML output:

# Breakfast: Upma
# Lunch: Quinoa
# Dinner: Tomato Soup
# Snack: Apple
# Input 4 – Heart Disease
# Enter Name: David
# Enter Age: 55
# Enter Gender (Male/Female): Male
# Enter Height (cm): 170
# Enter Weight (kg): 85
# Enter Activity Level (sedentary/light/moderate/active): sedentary
# Enter Goal (Weight Loss/Weight Gain/Maintenance): Weight Loss
# Enter Diet Type (Vegetarian/Vegan/Non-Vegetarian): Vegetarian
# Enter Health Condition (None/Diabetes/Heart Disease): Heart Disease

# Expected ML output:

# Breakfast: Oats
# Lunch: Chapati
# Dinner: Vegetable Soup
# Snack: Apple