import joblib
import numpy as np

# Load trained model
import os
import joblib
import numpy as np

# Absolute path to the model
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "best_random_forest.pkl"
)



def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    """
    Predict the best crop based on soil and weather conditions.
    """

    input_data = np.array([[

        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall

    ]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)
    confidence = probability.max() * 100

    return prediction[0], confidence


# Test Prediction
if __name__ == "__main__":

    crop = predict_crop(
        90,
        42,
        43,
        20.8,
        82,
        6.5,
        202
    )

    print("Recommended Crop:", crop)