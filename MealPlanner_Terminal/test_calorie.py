from calorie import *

bmi = calculate_bmi(70, 170)

print("BMI:", bmi)

print(
    "Status:",
    bmi_category(bmi)
)

bmr = calculate_bmr(
    70,
    170,
    25,
    "male"
)

print("BMR:", round(bmr))

tdee = calculate_tdee(
    bmr,
    "moderate"
)

print("TDEE:", round(tdee))

print(
    "Target Calories:",
    calorie_goal(
        tdee,
        "weight loss"
    )
)