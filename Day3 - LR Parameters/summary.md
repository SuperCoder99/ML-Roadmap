
<body>
  <h1>✅ Day 3 Summary – Linear Regression & Datasets in scikit-learn</h1>

  <h2>📌 Topics Covered:</h2>
  <ul>
    <li>Loading and exploring datasets (<code>fetch_california_housing</code>, <code>load_diabetes</code>)</li>
    <li>Building and evaluating <strong>Linear Regression</strong> models using scikit-learn</li>
    <li>Metrics: R² Score, Mean Absolute Error (MAE), Mean Squared Error (MSE)</li>
    <li>Visualizing model predictions vs actual values using matplotlib</li>
  </ul>

  <h2>🛠️ Model Implementation & Evaluation:</h2>
  <ul>
    <li>Imported datasets and split into train/test sets</li>
    <li>Trained Linear Regression models on multiple features</li>
    <li>Calculated performance metrics:</li>
  </ul>
  
```
California Housing:
  R2 Score: 0.5080
  Mean Absolute Error: 0.6102
  Mean Squared Error: 0.6599

Diabetes:
  R2 Score: 0.3941
  Mean Absolute Error: 49.5620
  Mean Squared Error: 3627.1428
```
  
  <ul>
    <li>Highlighted importance of using all features for improved prediction</li>
  </ul>

  <h2>📊 Visualization:</h2>
  <ul>
    <li>Plotted predicted vs actual target values</li>
    <li>Scatter plot for feature vs actual values + predicted regression line</li>
    <li>Used matplotlib’s <code>scatter()</code>, <code>plot()</code>, <code>xlabel()</code>, <code>ylabel()</code>, <code>title()</code>, <code>legend()</code>, and <code>grid()</code></li>
  </ul>
  <h2>📈 Key Takeaways:</h2>
  <ul>
    <li>Linear Regression is sensitive to feature selection and dataset quality</li>
    <li>Multiple features improve model accuracy over single-feature input</li>
    <li>Model performance can be improved further by feature scaling, regularization, or advanced models</li>
    <li>Visualizations are crucial to understand model fit and errors</li>
  </ul>
</body>
</html>
