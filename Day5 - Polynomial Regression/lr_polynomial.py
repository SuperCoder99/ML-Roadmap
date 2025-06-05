from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from graph_functions import *

housing = fetch_california_housing()
X = housing.data[:, 0].reshape(-1, 1)
y = housing.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 12, shuffle = True)

poly = PolynomialFeatures(degree=3)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model = LinearRegression()
model.fit(X_train_poly, y_train)

y_pred = model.predict(X_test_poly)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"R2 Score: {r2:.4f}")
print(f"Mean Absolute Error: {mae:.4f}")
print(f"Mean Squared Error: {mse:.4f}")
print("Coefficients:", [f"{val:.4f}" for val in model.coef_])
print("Intercept:", f"{model.intercept_:.4f}")

plot_linear_regression(X_test, y_test, y_pred)