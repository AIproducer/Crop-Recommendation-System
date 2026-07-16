from src.preprocessing import *

# Load dataset
df = load_data("data/processed/crop_processed.csv")

# Split features and target
X, y = split_features_target(df)

# Encode labels
y_encoded, encoder = encode_labels(y)

# Split dataset
X_train, X_test, y_train, y_test = split_dataset(X, y_encoded)

print("Training Features:", X_train.shape)
print("Testing Features :", X_test.shape)
print("Training Labels  :", y_train.shape)
print("Testing Labels   :", y_test.shape)

print("\nCrop Classes:")
print(encoder.classes_)