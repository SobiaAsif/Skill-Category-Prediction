import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("data/skill-scarcity-index.csv")

# Drop unnecessary columns
df = df.drop(columns=["snapshot_date", "skill_name"])

# Fill missing values
df["median_days_open"] = df["median_days_open"].fillna(
    df["median_days_open"].median()
)

df["salary_premium_pct"] = df["salary_premium_pct"].fillna(
    df["salary_premium_pct"].median()
)

# Features and target
X = df.drop(columns="category")
y = df["category"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier(n_neighbors=3))
])

# Train model
pipeline.fit(X_train, y_train)

# Predict
y_pred = pipeline.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}\n")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(
    pipeline,
    "models/skill_category_pipeline.pkl"
)

print("Pipeline saved successfully!")