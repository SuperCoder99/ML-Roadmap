# 🧠 Day 1 – Introduction to Machine Learning

## ✅ What I Learned

### 📌 What is Machine Learning?
- Machine Learning (ML) is the ability of computers to **learn patterns** from data without being explicitly programmed.
- Goal: Make **predictions or decisions** using historical data.

---

### 🔧 Types of Machine Learning
1. **Supervised Learning**  
   - Data has **input (X)** and **known output (Y)**  
   - Examples: Classification, Regression  
   - Used today

2. **Unsupervised Learning**  
   - Only **input data (X)** — no labels  
   - Goal: Find hidden patterns (e.g., clustering)

3. **Reinforcement Learning**  
   - Learning by **trial and error** with rewards  
   - Used in games, robotics, etc.

---

### 🌼 Iris Dataset
- Classic ML dataset: 150 flowers, 3 species (`setosa`, `versicolor`, `virginica`)
- 4 features per sample:
  - sepal length
  - sepal width
  - petal length
  - petal width

---

### 🔍 What I Did
- Loaded Iris dataset using `sklearn.datasets`
- Split into train/test using `train_test_split()`
- Trained a **Logistic Regression** model
- Evaluated accuracy on test set

---

### ✅ Output
- Model Accuracy: **100%** (on current split)
- Reason: Clean, separable dataset

---

### 💡 Key Takeaways
- Logistic Regression works well for **multiclass classification**
- Start simple → understand basic flow: load → split → train → predict → evaluate
- 100% accuracy is OK here, but won’t happen always


