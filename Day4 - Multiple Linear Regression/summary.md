<h1>📊 Day 4 – Multiple Linear Regression</h1>

<p>This project demonstrates how to implement <strong>Multiple Linear Regression</strong> using the <strong>California Housing Dataset</strong>.</p>

<hr>

<h2>✅ Objectives</h2>
<ul>
  <li>Implement multiple linear regression with <code>sklearn</code></li>
  <li>Use a real-world dataset (California Housing)</li>
  <li>Evaluate model performance</li>
  <li>Visualize predictions and residuals</li>
</ul>

<hr>

<h2>📁 Dataset</h2>
<p><strong>California Housing Dataset</strong><br>
<code>X</code>: 8 features (e.g., population, average rooms, income, etc.)<br>
<code>y</code>: Median house value</p>

<hr>

<h2>🧠 ML Workflow</h2>
<ol>
  <li>Import dataset using <code>fetch_california_housing()</code></li>
  <li>Split data using <code>train_test_split()</code></li>
  <li>Train model using <code>LinearRegression()</code></li>
  <li>Predict and evaluate:
    <ul>
      <li><code>r2_score</code></li>
      <li><code>mean_absolute_error</code></li>
      <li><code>mean_squared_error</code></li>
    </ul>
  </li>
  <li>Plot:
    <ul>
      <li>Actual vs Predicted</li>
      <li>Residuals</li>
    </ul>
  </li>
</ol>

<hr>

<h2>📈 Metrics</h2>
<table border="1" cellpadding="5">
  <tr><th>Metric</th><th>Value</th></tr>
  <tr><td>R² Score</td><td>~0.63</td></tr>
  <tr><td>MAE</td><td>~0.52</td></tr>
  <tr><td>MSE</td><td>~0.49</td></tr>
</table>

<hr>

<h2>📉 Visualizations</h2>
<ul>
  <li><strong>Scatter plot</strong> of Actual vs Predicted house values</li>
  <li><strong>Residual plot</strong> to check prediction errors</li>
</ul>

---

<h2>🚀 Output Sample</h2>
<pre>
R2 Score: 0.6324
Mean Absolute Error: 0.5203
Mean Squared Error: 0.4931
Coefficients: ['0.4372', '0.0131', '-0.0407', '0.8560', '-1.1786', '4.4602', '-0.0118', '-0.9293']
Intercept: -37.2192
</pre>

<hr>

<h2>📌 Conclusion</h2>
<p>Multiple Linear Regression works for moderately predictive tasks but may struggle with non-linearity or complex feature relationships.</p>
