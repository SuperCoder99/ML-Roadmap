from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from graph_functions import *
import numpy as np

x = np.array([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])
y = np.array([7, 10, 15, 19, 21, 27, 31, 35, 38, 42, 47, 50, 54, 59, 62])
X = [[val] for val in x]

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
m = model.coef_[0]
c = model.intercept_
mse = mean_squared_error(y, y_pred)

print(f"Line : Y = {m:.3f}X + ({c:.3f}) \nPredicted Y : {np.round(y_pred, 3)}\nMSE : {mse:.3f}")
plot_linear_regression(X, y, y_pred, label_data="Actual Data", label_plot="Predicted Line", title="Linear Regression: Actual vs Predicted", x_label="X", y_label="Y", color_data='blue', color_plot='red')


