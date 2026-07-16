import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def load_data(filepath):
    """
    Load dataset from CSV file.
    """
    df = pd.read_csv(filepath)
    return df


def split_features_target(df):
    """
    Separate input features and target.
    """
    X = df.drop("label", axis=1)
    y = df["label"]
    return X, y


def encode_labels(y):
    """
    Encode crop labels.
    """
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)
    return y_encoded, encoder


def split_dataset(X, y):
    """
    Split dataset into training and testing sets.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test