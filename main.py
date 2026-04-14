from src.data_preprocessing import load_data, preprocess_data
from src.train_model import train_model
from src.evaluate_model import evaluate_model
from src.predict import predict_failure
from src.visualize import plot_confusion_matrix


def main():
    print("=" * 60)
    print("AI-Powered Predictive Maintenance System for IoT Devices")
    print("=" * 60)

    # Step 1: Load Dataset
    print("\n[1] Loading Dataset...")
    data = load_data("data/raw/predictive_maintenance.csv")

    # Step 2: Preprocess Data
    print("\n[2] Preprocessing Data...")
    X_train, X_test, y_train, y_test = preprocess_data(data)

    # Step 3: Train Model
    print("\n[3] Training Model...")
    model = train_model(X_train, y_train)

    # Step 4: Evaluate Model
    print("\n[4] Evaluating Model...")
    y_pred = evaluate_model(model, X_test, y_test)

    # Step 5: Generate Predictions
    print("\n[5] Generating Predictions...")
    predict_failure(model, X_test)

    # Step 6: Visualize Results
    print("\n[6] Generating Visualizations...")
    plot_confusion_matrix(y_test, y_pred)

    print("\n✅ Project executed successfully!")


if __name__ == "__main__":
    main()