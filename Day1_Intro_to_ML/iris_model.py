from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
X, Y = iris.data, iris.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

print(f"Model Accuracy: {accuracy_score(Y_test, Y_pred) * 100}%")
