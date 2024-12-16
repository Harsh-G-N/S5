import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('advertising.csv')

# print("\nsimple regression\n-------------------------------")
# X = data[['TV']]  
# y = data['Sales']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = LinearRegression()

# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print(f"Mean Squared Error: {mse}")
# print(f"R-squared Score: {r2}")

# unseen_data = float(input("Enter a value for prediction: "))
# unseen_data = pd.DataFrame([[unseen_data]],columns=['TV'])
# prediction = model.predict(unseen_data)
# print(f"The predicted value for {unseen_data.iloc[0]} is: {prediction[0]}")

# plt.figure(figsize=(10, 6))

# plt.scatter(X, y, color='blue', label='Actual Sales')

# plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Sales')
# plt.scatter(unseen_data.iloc[0], prediction[0], color='green', marker='o', s=100, label='New Prediction')
# plt.title('TV Advertising Budget vs Sales')
# plt.xlabel('TV Advertising Budget ($)')
# plt.ylabel('Sales')
# plt.legend()
# plt.show()

# print("\nmultivariable regression\n----------------------------------")
# X = data[['TV', 'Radio', 'Newspaper']]  # Multiple features
# y = data['Sales']  # Target variable

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = LinearRegression()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print(f"Mean Squared Error: {mse}")
# print(f"R-squared Score: {r2}")

# tv_input = float(input("Enter TV advertising budget: "))
# radio_input = float(input("Enter Radio advertising budget: "))
# newspaper_input = float(input("Enter Newspaper advertising budget: "))

# unseen_data = pd.DataFrame([[tv_input, radio_input, newspaper_input]], columns=['TV', 'Radio', 'Newspaper'])

# prediction = model.predict(unseen_data)
# print(f"The predicted sales for TV={tv_input}, Radio={radio_input}, Newspaper={newspaper_input} is: {prediction[0]}")

# plt.figure(figsize=(10, 6))
# plt.scatter(y_test, y_pred, color='blue', label='Predicted Sales')

# plt.scatter([prediction[0]], [prediction[0]], color='green', marker='o', s=100, label='User Prediction')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2, label='Perfect Prediction')

# plt.title('Actual vs Predicted Sales')
# plt.xlabel('Actual Sales')
# plt.ylabel('Predicted Sales')
# plt.legend()

#plt.show()

print("\npolynomial regression\n-----------------------")
X = data[['TV']]
y = data['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

degree = 2  
poly_features = PolynomialFeatures(degree=degree)
X_poly_train = poly_features.fit_transform(X_train)
X_poly_test = poly_features.transform(X_test)

print(X_poly_train)

model = LinearRegression()
model.fit(X_poly_train, y_train)

y_pred = model.predict(X_poly_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

tv_input = float(input("Enter TV advertising budget: "))

unseen_data = pd.DataFrame([[tv_input]], columns=['TV'])

unseen_data_poly = poly_features.transform(unseen_data)

prediction = model.predict(unseen_data_poly)
print(f"The predicted sales for TV={tv_input} is: {prediction[0]}")

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Sales')

X_grid = np.arange(X['TV'].min(), X['TV'].max(), 1).reshape(-1, 1)
y_grid = model.predict(poly_features.transform(pd.DataFrame(X_grid, columns=['TV'])))
plt.plot(X_grid, y_grid, color='red', label='Polynomial Regression Curve')

plt.scatter(tv_input, prediction, color='green', marker='o', s=100, label='User Prediction')

plt.title('Polynomial Regression of Sales vs TV Advertising')
plt.xlabel('TV Advertising Budget')
plt.ylabel('Sales')
plt.legend()

plt.show()