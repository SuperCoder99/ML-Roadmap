<h2>✅ Day 2 Summary – Linear Regression (From Scratch + scikit-learn)</h2>

<h3>📌 Topics Covered:</h3>
<ul>
  <li>Linear Regression Theory</li>
  <li>Manual Implementation (Analytical Method)</li>
  <li>Evaluation with Mean Squared Error (MSE)</li>
  <li>Data Visualization using <code>matplotlib</code></li>
  <li>Linear Regression using <code>scikit-learn</code></li>
</ul>

---

<h3>🛠️ Manual Implementation (From Scratch):</h3>
<ul>
  <li>Calculated:
    <ul>
      <li>Mean of <code>x</code> and <code>y</code></li>
      <li>Slope: <code>m = Σ[(x - x̄)(y - ȳ)] / Σ[(x - x̄)^2]</code></li>
      <li>Intercept: <code>c = ȳ - m·x̄</code></li>
    </ul>
  </li>
  <li>Predicted values using: <code>ŷ = m * x + c</code></li>
  <li>Computed MSE: <code>MSE = (1/n) * Σ(ŷ - y)^2</code></li>
</ul>

---

<h3>📊 Matplotlib Plot:</h3>
<ul>
  <li>Plotted actual data (blue dots)</li>
  <li>Plotted predicted line (red line)</li>
  <li>Used:
    <ul>
      <li><code>plt.legend()</code></li>
      <li><code>plt.grid(True)</code></li>
      <li><code>plt.xlabel()</code>, <code>plt.ylabel()</code>, <code>plt.title()</code></li>
      <li><code>plt.show()</code></li>
    </ul>
  </li>
</ul>

---

<h3>🤖 Using scikit-learn:</h3>
<ul>
  <li>Imported: <code>LinearRegression</code> and <code>mean_squared_error</code></li>
  <li>Reshaped input: <code>X = [[val] for val in x]</code></li>
  <li>Trained model: <code>model.fit(X, y)</code></li>
  <li>Predicted: <code>model.predict(X)</code></li>
  <li>Extracted:
    <ul>
      <li>Slope: <code>model.coef_[0]</code></li>
      <li>Intercept: <code>model.intercept_</code></li>
    </ul>
  </li>
  <li>Calculated MSE using <code>mean_squared_error</code></li>
  <li>Plotted results with <code>matplotlib</code></li>
</ul>

---

<h3>📈 Final Result:</h3>

```
x = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
y = [7, 10, 15, 19, 21, 27, 31, 35, 38, 42, 47, 50, 54, 59, 62]
Line : Y = 1.988X + (0.679) 
Predicted Y : [6.642, 10.617, 14.592, 18.567, 22.542, 26.517, 30.492, 34.467, 38.442, 42.417, 46.392, 50.367, 54.342, 58.317, 62.292]
MSE : 0.371
