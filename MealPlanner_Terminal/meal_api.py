from flask import Flask, request, jsonify

from recommender import recommend_meals

app = Flask(__name__)

@app.route('/meal-plan', methods=['POST'])
def meal_plan():

    data = request.json

    goal = data.get("goal")

    diet = data.get("diet")

    health = data.get(
        "health_condition",
        "None"
    )

    meals = recommend_meals(
        goal,
        diet,
        health
    )

    return jsonify(meals)

if __name__ == "__main__":

    app.run(debug=True)
    
# {
#     "goal":"Weight Loss",
#     "diet":"Vegetarian",
#     "health_condition":"None"
# }