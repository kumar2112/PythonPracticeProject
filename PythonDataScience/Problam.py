# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 2: Load the Data
data = pd.read_csv('house_prices.csv')  # Replace with your dataset path
print(data.head())

# Step 3: Data Exploration
print(data.describe())
print(data.info())

# Step 4: Data Preprocessing
# Handle missing values (if any)
data = data.dropna()  # Or use data.fillna() with imputation

# Convert categorical variables to numerical (if any)
data = pd.get_dummies(data, drop_first=True)

# Step 5: Split Data
X = data.drop('price', axis=1)  # Features (excluding target variable 'price')
y = data['price']  # Target variable (house prices)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Build the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Evaluate the Model
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Step 8: Make Predictions
sample_data = X_test.iloc[0:5]  # Taking 5 sample data points
sample_predictions = model.predict(sample_data)

print(f'Predicted Prices: {sample_predictions}')
