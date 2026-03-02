import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

dataset = pd.read_csv(r"E:\Work\Programs\Python\AI\Machine Learning\Projects\House Price Predictator\data\cityhome_data.csv")
dataset.dropna(inplace=True)

le = LabelEncoder()
dataset["House_condition(Encoded)"] = le.fit_transform(dataset["House_Condition"])
dataset["Location(Encoded)"] = le.fit_transform(dataset["Location"])

columns = dataset[["Size_SqFt", "Bedrooms", "Bathrooms", "Location(Encoded)", 
                   "House_condition(Encoded)", "Year_Built"]]

X = columns
y = dataset["Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predicted_Test = model.predict(X_test)

mse = mean_squared_error(y_test, predicted_Test)
mae = mean_absolute_error(y_test, predicted_Test)
r2 = r2_score(y_test, predicted_Test)

print("Mse: ", round(mse))
print("Rmse: ", round(np.sqrt(mse)))
print("Mae: ", round(mae))
print("R2 score: ", r2)

# --- FIX START ---
# 1. Convert y_test to a simple list of numbers (removes index issues)
y_test_values = y_test.values

# 2. Create a RANGE of numbers (0, 1, 2...) matching the total count
# This fixes the "x and y must be same size" error
total_samples = len(y_test_values)
subset_range = range(total_samples)

plt.figure(figsize=(12, 6))
plt.scatter(subset_range, y_test_values, color='blue', label='Actual Price', s=70, alpha=0.7)
plt.scatter(subset_range, predicted_Test, color='red', label='Predicted Price', s=70, marker='x')

for i in subset_range:
    plt.plot([i, i], [y_test_values[i], predicted_Test[i]], color='green', linestyle='--', alpha=0.5)

plt.title(f"Actual vs Predicted Prices ({total_samples} Samples)")
plt.xlabel("Sample Index")
plt.ylabel("House Price")
plt.legend()
plt.grid(True)
plt.show()
