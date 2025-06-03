from graph_functions import *

def predict_y(x, m, c):
  return [m*value + c for value in x]

def MSE(pred_y, true_y):
  return (sum((pred_y[i] - true_y[i]) ** 2 for i in range(len(pred_y)))) / len(pred_y)

x = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
y = [7, 10, 15, 19, 21, 27, 31, 35, 38, 42, 47, 50, 54, 59, 62]
n = len(x)
mean_x = sum(x) / n
mean_y = sum(y) / n
sum_xy = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
sum_x2 = sum((x[i] - mean_x) ** 2 for i in range(n))

m = sum_xy / sum_x2
c = mean_y - m * mean_x

pred_y = [float(f"{value:.3f}") for value in predict_y(x, m, c)]
mse = MSE(pred_y, y)
print("ANALYTICAL METHOD:")
print(f"Line : Y = {m:.3f}X + ({c:.3f}) \nPredicted Y : {pred_y}\nMSE : {mse:.3f}")

plot_linear_regression(x, y, pred_y, label_data="Actual Data", label_plot="Predicted Line", title="Linear Regression: Actual vs Predicted", x_label="X", y_label="Y", color_data="blue", color_plot="red")
