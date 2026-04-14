from sklearn.ensemble import RandomForestClassifier
import joblib
import os


def train_model(X_train, y_train):
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/predictive_maintenance_model.pkl")

    print("Model saved in models/ directory.")
    return model