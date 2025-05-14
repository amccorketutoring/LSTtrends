# OLS Regression Example

## This example runs a simple OLS regression using LST as the dependent variable and NDVI, building density, slope, and aspect as predictors.

```python
from lsttrends.analysis import stats_ols
from pathlib import Path
import pandas as pd

csv_path = Path("data/Knox_UHI_Zonal_Stats_STRM.csv")
df = pd.read_csv(csv_path)

features = ["NDVI", "BuildingDensity", "Slope", "Aspect"]
target = "LST_Celsius"

model, results = stats_ols.run_ols_regression(df, target=target, predictors=features)
print(results.summary())

# Visualize outputs
output_path = Path("outputs/OLS_Residuals.png")
stats_ols.plot_residuals(df, results, output_path=output_path)
```