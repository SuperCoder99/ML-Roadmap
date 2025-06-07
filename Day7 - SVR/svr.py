from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from graph_functions import *

def evaluate_model(name, y_true, y_pred):
  print(f"\n{name}")
  print(f"R2 Score: {r2_score(y_true, y_pred): .4f}")
  print(f"Mean Absolute Error: {mean_absolute_error(y_true, y_pred): .4f}")
  print(f"Mean Squared Error: {mean_squared_error(y_true, y_pred): .4f}")

housing = fetch_california_housing()
X, y = housing.data, housing.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

svr_linear = SVR(kernel='linear')
svr_linear.fit(X_train, y_train)
y_pred_linear = svr_linear.predict(X_test)
evaluate_model("SVR - Linear Kernel", y_test, y_pred_linear)

svr_rbf = SVR(kernel='rbf', C=10, epsilon=0.1, gamma=0.1)
svr_rbf.fit(X_train, y_train)
y_pred_rbf = svr_rbf.predict(X_test)
evaluate_model("SVR - RBF Kernel", y_test, y_pred_rbf)

plot_actual_vs_predicted(y_test, y_pred_linear)
