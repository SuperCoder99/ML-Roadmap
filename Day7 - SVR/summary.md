<h2>📊 Day 7 – Support Vector Regression (SVR)</h2>
<p>This project explores Support Vector Regression (SVR) using both linear and non-linear kernels to model housing prices from the California Housing dataset. The goal is to understand the power of SVR and kernel functions in capturing complex data patterns.</p>

<h3>✅ Objectives</h3>
<ul>
  <li>Understand the fundamentals of Support Vector Regression (SVR)</li>
  <li>Implement SVR using both <code>linear</code> and <code>rbf</code> (Radial Basis Function) kernels</li>
  <li>Compare performance of both kernels using regression metrics</li>
  <li>Visualize actual vs predicted values to assess model fit</li>
</ul>

<h3>📁 Dataset</h3>
<ul>
  <li>Dataset: California Housing (from <code>sklearn.datasets</code>)</li>
  <li>Features (X): 8 scaled features</li>
  <li>Target (y): Median house value</li>
</ul>

<h3>🧠 ML Workflow</h3>
<ul>
  <li>Load and scale the dataset using <code>StandardScaler</code></li>
  <li>Split into training and testing sets (80/20 split)</li>
  <li>Train two SVR models:
    <ul>
      <li><code>SVR(kernel='linear')</code></li>
      <li><code>SVR(kernel='rbf', C=10, epsilon=0.1, gamma=0.1)</code></li>
    </ul>
  </li>
  <li>Evaluate models using R², MAE, and MSE</li>
  <li>Visualize predictions with <code>plot_actual_vs_predicted()</code></li>
</ul>

<h3>📈 Metrics</h3>
<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr><th>Model</th><th>R² Score</th><th>MAE</th><th>MSE</th></tr>
  </thead>
  <tbody>
    <tr><td>SVR – Linear Kernel</td><td>0.5580</td><td>0.5120</td><td>0.5793</td></tr>
    <tr><td>SVR – RBF Kernel</td><td>0.7490</td><td>0.3817</td><td>0.3289</td></tr>
  </tbody>
</table>

<h3>📉 Visualizations</h3>
<ul>
  <li>Actual vs Predicted plot for SVR (Linear Kernel)</li>
  <li>(Optionally) Compare prediction plots of both kernels to understand non-linearity</li>
</ul>

<h3>🚀 Output Sample</h3>
<pre>
SVR - Linear Kernel
R2 Score:  0.5580
Mean Absolute Error:  0.5120
Mean Squared Error:  0.5793

SVR - RBF Kernel
R2 Score:  0.7490
Mean Absolute Error:  0.3817
Mean Squared Error:  0.3289
</pre>

<h3>📌 Conclusion</h3>
<p>The SVR model with the RBF kernel significantly outperformed the linear version, indicating non-linear relationships in the data. This experiment demonstrates how kernel methods can improve prediction accuracy by allowing the model to learn complex patterns.</p>
