# GWR Model Example

This example runs a Geographically Weighted Regression on LST data with selected predictors.

``` python from lsttrends.analysis import stats_gwr
from pathlib import Path
```

# Run the GWR model and output the local R² map
``` python
results = stats_gwr.run_gwr_model(save_plot=True, output_path=Path("outputs/GWR_Local_R2.png"))

# Show model summary
print(results.summary())
```