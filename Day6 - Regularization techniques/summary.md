<h2>📊 Day 6 – Regularization Techniques (ElasticNetCV)</h2>
<p>This project demonstrates how to apply regularization using the <code>ElasticNetCV</code> model, which combines both L1 (Lasso) and L2 (Ridge) penalties. The model is trained on the California Housing dataset with cross-validation to select the best hyperparameters.</p>

<h3>✅ Objectives</h3>
<ul>
  <li>Understand the concept of regularization: L1 (Lasso), L2 (Ridge), and ElasticNet</li>
  <li>Implement <code>ElasticNetCV</code> with cross-validation to auto-select <code>alpha</code> and <code>l1_ratio</code></li>
  <li>Evaluate model performance using regression metrics</li>
  <li>Interpret the effect of regularization on coefficients</li>
</ul>

<h3>📁 Dataset</h3>
<ul>
  <li>Dataset: California Housing (from <code>sklearn.datasets</code>)</li>
  <li>Features (X): 8 numerical features (scaled)</li>
  <li>Target (y): Median house value</li>
</ul>

<h3>🧠 ML Workflow</h3>
<ul>
  <li>Load dataset and split into train/test sets (90/10 split)</li>
  <li>Scale features using <code>StandardScaler</code></li>
  <li>Train model using <code>ElasticNetCV</code> with:
    <ul>
      <li><code>alphas = logspace(-4, 1, 20)</code></li>
      <li><code>l1_ratio = [0.1, 0.3, 0.5, 0.7, 0.9, 1.0]</code></li>
      <li>5-fold cross-validation</li>
    </ul>
  </li>
  <li>Predict on test set</li>
  <li>Evaluate using MAE, MSE, and R²</li>
</ul>

<h3>📈 Metrics</h3>
<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr><th>Metric</th><th>Value</th></tr>
  </thead>
  <tbody>
    <tr><td>R² Score</td><td>0.6316</td></tr>
    <tr><td>Mean Absolute Error</td><td>0.5211</td></tr>
    <tr><td>Mean Squared Error</td><td>0.4941</td></tr>
  </tbody>
</table>

<h3>📉 Visualizations</h3>
<ul>
  <li>Actual vs Predicted plot for test set using <code>plot_actual_vs_predicted()</code></li>
</ul>

<h3>🚀 Output Sample</h3>
<pre>
R2 Score: 0.6316
Mean Absolute Error: 0.5211
Mean Squared Error: 0.4941
Coefficients: ['0.8103', '0.1212', '-0.2358', '0.2769', '-0.0035', '-0.0375', '-0.8787', '-0.8493']
Intercept: 2.0681
</pre>

<h3>📌 Conclusion</h3>
<p>ElasticNetCV provided a well-balanced regularized model, achieving better generalization by reducing overfitting. The combination of L1 and L2 helped shrink less important features while preserving predictive performance. This technique is especially useful when dealing with multicollinearity and sparse features.</p>
