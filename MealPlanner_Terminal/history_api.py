from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/history')
def history():

    df = pd.read_csv("history.csv")

    result = df[
        [
            "Name",
            "Goal",
            "BMI"
        ]
    ]

    return jsonify(
        result.to_dict(
            orient="records"
        )
    )

if __name__ == "__main__":
    app.run(debug=True)