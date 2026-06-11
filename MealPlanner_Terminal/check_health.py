import joblib

health_encoder = joblib.load(
    "health_encoder.pkl"
)

print(
    health_encoder.classes_
)
