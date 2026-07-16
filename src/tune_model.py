import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier


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

param_grid = {

    "n_estimators":[100,200,300],

    "max_depth":[None,10,20],

    "min_samples_split":[2,5],

    "min_samples_leaf":[1,2]

}

grid = GridSearchCV(

    RandomForestClassifier(random_state=42),

    param_grid,

    cv=5,

    scoring="accuracy",

    n_jobs=-1

)

grid.fit(X_train,y_train)

print(grid.best_params_)

print(grid.best_score_)

joblib.dump(grid.best_estimator_,"models/best_random_forest.pkl")

print("Best Tuned Model Saved")