from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
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

plt.scatter(X, y, color='blue', label='Actual Data')  
plt.plot(X, y_pred, color='red', label='Predicted Line') 
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression: Actual vs Predicted")
plt.legend()
plt.grid(True)

print(f"Line : Y = {m:.3f}X + ({c:.3f}) \nPredicted Y : {np.round(y_pred, 3)}\nMSE : {mse:.3f}")
plt.show()



