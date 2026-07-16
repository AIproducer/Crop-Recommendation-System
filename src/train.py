import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


# Load Dataset
df = pd.read_csv("data/processed/crop_processed.csv")

X = df.drop("label", axis=1)
y = df["label"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Models
models = {

    "Logistic Regression": LogisticRegression(max_iter=1000),

    "Decision Tree": DecisionTreeClassifier(random_state=42),

    "Random Forest": RandomForestClassifier(random_state=42),

    "KNN": KNeighborsClassifier(),

    "SVM": SVC(),

    "Gradient Boosting": GradientBoostingClassifier(random_state=42),

    "Extra Trees": ExtraTreesClassifier(random_state=42)

}

results = []

best_accuracy = 0
best_model = None

for name, model in models.items():

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    results.append([name, accuracy])

    print(name, accuracy)

    if accuracy > best_accuracy:

        best_accuracy = accuracy
        best_model = model

results = pd.DataFrame(results, columns=["Model","Accuracy"])

print(results.sort_values("Accuracy", ascending=False))

os.makedirs("models", exist_ok=True)

joblib.dump(best_model, "models/crop_model.pkl")

print("Best Model Saved")