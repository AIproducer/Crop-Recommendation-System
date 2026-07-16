import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import cross_val_score


df = pd.read_csv("data/processed/crop_processed.csv")

X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

model = joblib.load("models/best_random_forest.pkl")

prediction = model.predict(X_test)

print(classification_report(y_test,prediction))

scores = cross_val_score(model,X,y,cv=10)

print("Scores:",scores)

print("Average:",scores.mean())

print("Std:",scores.std())


feature_importance = pd.DataFrame({

    "Feature":X.columns,

    "Importance":model.feature_importances_

})

feature_importance = feature_importance.sort_values(

    by="Importance",

    ascending=False

)

print(feature_importance)

plt.figure(figsize=(8,5))

plt.bar(

    feature_importance["Feature"],

    feature_importance["Importance"]

)

plt.tight_layout()

plt.savefig("images/feature_importance.png")

plt.show()


ConfusionMatrixDisplay.from_estimator(

    model,

    X_test,

    y_test,

    xticks_rotation=90

)

plt.tight_layout()

plt.savefig("images/confusion_matrix.png")

plt.show()