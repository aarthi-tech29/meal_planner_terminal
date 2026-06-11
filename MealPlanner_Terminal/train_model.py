import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

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
# Feature Scaling
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
# Random Forest Model
# =========================

model = RandomForestClassifier(
    n_estimators=500,
    max_depth=20,
    min_samples_split=2,
    min_samples_leaf=1,
    class_weight="balanced",
    random_state=42
)

# =========================
# Train Model
# =========================

model.fit(
    X_train,
    y_train
)

# =========================
# Predictions
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

print("\n========== MODEL RESULTS ==========")

print(
    "Accuracy:",
    round(
        accuracy * 100,
        2
    ),
    "%"
)

print(
    "\nDataset Size:",
    len(df)
)

print(
    "\nCategory Distribution:"
)

print(
    df["Category"].value_counts()
)

# =========================
# Save Model
# =========================

joblib.dump(
    model,
    "meal_model.pkl"
)

joblib.dump(
    scaler,
    "scaler.pkl"
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
    "\nModel Saved Successfully"
)