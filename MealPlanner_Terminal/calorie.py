def calculate_bmi(weight, height):

    h = height / 100

    bmi = weight / (h * h)

    return round(bmi, 2)


def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


def calculate_bmr(weight, height, age, gender):

    if gender.lower() == "male":

        return (
            10 * weight
            + 6.25 * height
            - 5 * age
            + 5
        )

    else:

        return (
            10 * weight
            + 6.25 * height
            - 5 * age
            - 161
        )


def calculate_tdee(bmr, activity_level):

    factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725
    }

    return round(
        bmr * factors.get(
            activity_level.lower(),
            1.2
        ),
        2
    )


def calorie_goal(tdee, goal):

    if goal.lower() == "weight loss":

        return round(tdee - 500)

    elif goal.lower() == "weight gain":

        return round(tdee + 500)

    else:

        return round(tdee)