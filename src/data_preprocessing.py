# src/data_preprocessing.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data(filepath):
    """
    Load the predictive maintenance dataset.
    """
    df = pd.read_csv(filepath)
    print("Dataset loaded successfully.")
    print("Dataset Shape:", df.shape)
    print("\nColumns:", list(df.columns))
    return df


def preprocess_data(df):
    """
    Preprocess the dataset for machine learning.
    """

    # Drop unnecessary columns
    df = df.drop(["UDI", "Product ID"], axis=1)

    # Convert categorical column 'Type' into numerical form
    df = pd.get_dummies(df, columns=["Type"], drop_first=True)

    # Define features and target
    X = df.drop("Machine failure", axis=1)
    y = df["Machine failure"]

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    print("\nPreprocessing completed successfully.")
    print("Training Data Shape:", X_train.shape)
    print("Testing Data Shape:", X_test.shape)

    return X_train, X_test, y_train, y_test