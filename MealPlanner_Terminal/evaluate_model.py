import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# =========================
# Load Dataset
# =========================

df = pd.read_csv("cleaned_foods.csv")

# =========================
# Handle Missing Values
# =========================

df["Health_Condition"] = df[
    "Health_Condition"
].fillna("None")

# =========================
# Encode Categorical Data
# =========================

diet_encoder = LabelEncoder()
health_encoder = LabelEncoder()

df["Diet_Type"] = diet_encoder.fit_transform(
    df["Diet_Type"]
)

df["Health_Condition"] = health_encoder.fit_transform(
    df["Health_Condition"]
)

# =========================
# Feature Engineering
# =========================

df["Calorie_Level"] = pd.cut(
    df["Calories"],
    bins=[0,150,300,1000],
    labels=[0,1,2]
)

# =========================
# Features & Target
# =========================

X = df[
    [
        "Calories",
        "Protein",
        "Carbs",
        "Fat",
        "Diet_Type",
        "Health_Condition",
        "Calorie_Level"
    ]
]

y = df["Category"]

# =========================
# Scaling
# =========================

scaler = StandardScaler()

X = scaler.fit_transform(X)

# =========================
# Train Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.15,
    random_state=42,
    stratify=y
)

# =========================
# Load Saved Model
# =========================

model = joblib.load(
    "meal_model.pkl"
)

# =========================
# Predictions
# =========================

predictions = model.predict(
    X_test
)

# =========================
# Evaluation
# =========================

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n========== MODEL EVALUATION ==========\n")

print(
    "Accuracy:",
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

print("\nConfusion Matrix:\n")

print(
    confusion_matrix(
        y_test,
        predictions
    )
)