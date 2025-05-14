# stats_ols Module

The `stats_ols` module provides tools for performing Ordinary Least Squares (OLS) regression analysis to explore the relationship between Land Surface Temperature (LST) and urban morphology variables.

## Functions

### `run_ols_regression(csv_path=None, target='LST_Celsius', predictors=['NDVI', 'BuildingDensity', 'Slope', 'Aspect'])`
Fits an OLS model using data loaded from the provided CSV path.

**Parameters:**
- `csv_path` (Path or str, optional): Path to the CSV file. If None, the default dataset will be used.
- `target` (str): The dependent variable (e.g., `'LST_Celsius'`).
- `predictors` (list of str): List of independent variables.

**Returns:**
- `model`: The `statsmodels` OLS model object.
- `results`: The fitted model results (summary, p-values, coefficients, R², etc.).

---

### `plot_residuals(df, results, output_path)`
Creates a scatter plot of residuals vs. fitted values.

**Parameters:**
- `df` (pd.DataFrame): DataFrame used for fitting the model.
- `results`: Output from the OLS model's `.fit()` method.
- `output_path` (str or Path): Path to save the resulting PNG plot.

---

## Example

```python
from lsttrends.analysis import stats_ols
from pathlib import Path
import pandas as pd

# Load data
csv_path = Path("data/Knox_UHI_Zonal_Stats_STRM.csv")
df = pd.read_csv(csv_path)

# Run regression
target = "LST_Celsius"
features = ["NDVI", "BuildingDensity", "Slope", "Aspect"]
model, results = stats_ols.run_ols_regression(csv_path=csv_path, target=target, predictors=features)

# Summary
print(results.summary())

# Save residual plot
output_path = Path("outputs/OLS_Regression_Residuals_vs_Fitted_Values.png")
stats_ols.plot_residuals(df, results, output_path)
