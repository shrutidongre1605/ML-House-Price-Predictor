import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load data
data = pd.read_csv("data/housing.csv")

# Convert text columns to numbers
le_location = LabelEncoder()
le_condition = LabelEncoder()
le_garage = LabelEncoder()

data["Location"] = le_location.fit_transform(data["Location"])
data["Condition"] = le_condition.fit_transform(data["Condition"])
data["Garage"] = le_garage.fit_transform(data["Garage"])

# Features and Target
X = data.drop("Price", axis=1)
y = data["Price"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)
print("MAE:", mae)

# Save Model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")

print("Model Saved Successfully!")