# src/train_model.py

from sklearn.ensemble import RandomForestClassifier
import joblib
import os


def train_model(X_train, y_train):
    """
    Train and save a Random Forest model for predictive maintenance.
    """

    print("Training Random Forest model...")

    # Initialize the model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    # Train the model
    model.fit(X_train, y_train)

    # Ensure the models directory exists
    os.makedirs("models", exist_ok=True)

    # Save the trained model
    model_path = "models/predictive_maintenance_model.pkl"
    joblib.dump(model, model_path)

    print(f"Model saved at: {model_path}")

    return model