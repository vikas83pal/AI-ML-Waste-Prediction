import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

data = pd.read_excel("data.xlsx", engine="openpyxl")

data.columns = data.columns.str.strip().str.lower()


data["estimated_waste"] = (
    data["daily_waste"] * data["since_last_pi"]
)

data["utilization_ratio"] = (
    data["estimated_waste"] / data["bin_capacity_k"]
)

# Drop bin_id
if "bin_id" in data.columns:
    data = data.drop(columns=["bin_id"])

X = data.drop("is_full", axis=1)
y = data["is_full"]

categorical_cols = ["location_type", "weather"]

numerical_cols = [
    "daily_waste",
    "since_last_pi",
    "festival_week",
    "bin_capacity_k",
    "estimated_waste",
    "utilization_ratio"
]


preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numerical_cols)
    ]
)


model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced"
)

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", model)
])


X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

joblib.dump(pipeline, "waste_prediction_model.pkl")

print("\nModel saved successfully.")
