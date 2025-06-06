<h2>📊 Day 5 – Multiple Linear Regression</h2>
<p>This project demonstrates how to implement Multiple Linear Regression using a sample dataset.</p>

<h3>✅ Objectives</h3>
<ul>
  <li>Implement multiple linear regression with <code>sklearn</code></li>
  <li>Use a real-world dataset with multiple features</li>
  <li>Evaluate model performance using key metrics</li>
  <li>Understand model coefficients and intercept</li>
</ul>

<h3>📁 Dataset</h3>
<ul>
  <li>Features (X): 4 variables (example features from the dataset)</li>
  <li>Target (y): Continuous target variable</li>
</ul>

<h3>🧠 ML Workflow</h3>
<ul>
  <li>Import dataset and split into train and test sets</li>
  <li>Train model using <code>LinearRegression()</code></li>
  <li>Predict on test data</li>
  <li>Evaluate using:
    <ul>
      <li><code>r2_score</code></li>
      <li><code>mean_absolute_error</code></li>
      <li><code>mean_squared_error</code></li>
    </ul>
  </li>
  <li>Examine model coefficients and intercept</li>
</ul>

<h3>📈 Metrics</h3>
<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr><th>Metric</th><th>Value</th></tr>
  </thead>
  <tbody>
    <tr><td>R² Score</td><td>0.5223</td></tr>
    <tr><td>Mean Absolute Error</td><td>0.5998</td></tr>
    <tr><td>Mean Squared Error</td><td>0.6407</td></tr>
  </tbody>
</table>

<h3>📉 Visualizations</h3>
<ul>
  <li>(Optional) Plot actual vs predicted values to visualize fit</li>
  <li>(Optional) Plot residuals to assess errors</li>
</ul>

<h3>🚀 Output Sample</h3>
<pre>
R2 Score: 0.5223
Mean Absolute Error: 0.5998
Mean Squared Error: 0.6407
Coefficients: ['0.0000', '0.1363', '0.0623', '-0.0036']
Intercept: 0.7848
</pre>

<h3>📌 Conclusion</h3>
<p>Multiple Linear Regression provides moderate predictive performance. Model interpretation via coefficients helps understand feature impact. Further improvements may require advanced techniques like regularization or non-linear models.</p>
