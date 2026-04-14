import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data(filepath):
    df = pd.read_csv(filepath)
    print("Dataset Shape:", df.shape)
    return df


def preprocess_data(df):
    # Drop unnecessary columns
    df = df.drop(["UDI", "Product ID"], axis=1)

    # Convert categorical data
    df = pd.get_dummies(df, columns=["Type"], drop_first=True)

    # Define features and target
    X = df.drop("Machine failure", axis=1)
    y = df["Machine failure"]

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    print("Preprocessing Completed.")
    return X_train, X_test, y_train, y_test