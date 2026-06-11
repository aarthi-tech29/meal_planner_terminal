import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Load Dataset
df = pd.read_csv("history.csv")
df["Health_Condition"] = df["Health_Condition"].fillna("None")

# Encode Features
goal_encoder = LabelEncoder()
diet_encoder = LabelEncoder()
health_encoder = LabelEncoder()

df["Goal"] = goal_encoder.fit_transform(
    df["Goal"]
)

df["Diet_Type"] = diet_encoder.fit_transform(
    df["Diet_Type"]
)

df["Health_Condition"] = health_encoder.fit_transform(
    df["Health_Condition"]
)

# Features
X = df[
    [
        "Goal",
        "BMI",
        "Diet_Type",
        "Health_Condition"
    ]
]

# Target
y = df["Dinner"]

# Encode Target
dinner_encoder = LabelEncoder()

y = dinner_encoder.fit_transform(y)

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

# Train
model.fit(
    X_train,
    y_train
)

# Predict
predictions = model.predict(
    X_test
)

# Accuracy
accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n========== DINNER MODEL ==========\n")

print(
    "Accuracy:",
    round(
        accuracy * 100,
        2
    ),
    "%"
)

print(
    classification_report(
        y_test,
        predictions,
        zero_division=0
    )
)

# Save Model
joblib.dump(
    model,
    "dinner_model.pkl"
)

joblib.dump(
    dinner_encoder,
    "dinner_encoder.pkl"
)

joblib.dump(
    goal_encoder,
    "goal_encoder.pkl"
)

joblib.dump(
    diet_encoder,
    "diet_encoder.pkl"
)

joblib.dump(
    health_encoder,
    "health_encoder.pkl"
)

print(
    "\nDinner Model Saved Successfully"
)