import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# =========================
# Load History Dataset
# =========================

df = pd.read_csv("history.csv")
df["Health_Condition"] = df["Health_Condition"].fillna("None")

# =========================
# Encode Goal
# =========================

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

# =========================
# Features
# =========================

X = df[
    [
        "Goal",
        "BMI",
        "Diet_Type",
        "Health_Condition"
    ]
]

# =========================
# Target
# =========================

y = df["Breakfast"]

# =========================
# Encode Breakfast Labels
# =========================

breakfast_encoder = LabelEncoder()

y = breakfast_encoder.fit_transform(y)

# =========================
# Train Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# Random Forest
# =========================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# =========================
# Prediction
# =========================

predictions = model.predict(
    X_test
)

# =========================
# Accuracy
# =========================

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n========== HISTORY MODEL ==========\n")

print(
    "Breakfast Prediction Accuracy:",
    round(
        accuracy * 100,
        2
    ),
    "%"
)

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        predictions
    )
)

# =========================
# Save Model
# =========================

joblib.dump(
    model,
    "breakfast_model.pkl"
)

joblib.dump(
    goal_encoder,
    "goal_encoder.pkl"
)

joblib.dump(
    breakfast_encoder,
    "breakfast_encoder.pkl"
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
    "\nBreakfast Model Saved Successfully"
)