import pandas as pd
import os


def predict_failure(model, X_test):
    """Generate and save predictions."""
    predictions = model.predict(X_test)

    df = pd.DataFrame({
        "Predicted Failure": predictions
    })

    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/predictions.csv", index=False)

    print("Predictions saved to outputs/predictions.csv")