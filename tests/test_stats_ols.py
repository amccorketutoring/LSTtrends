# tests/test_stats_ols.py

from pathlib import Path
import pandas as pd
from lsttrends.analysis import stats_ols

# Set up paths
HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent / "data"
OUTPUT_DIR = HERE.parent / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load data
csv_path = DATA_DIR / "Knox_UHI_Zonal_Stats_STRM.csv"
df = pd.read_csv(csv_path)

# Define regression inputs
target = "LST_Celsius"
features = ["NDVI", "BuildingDensity", "Slope", "Aspect"]

# Run regression
print("▶️ Running OLS regression...")
model, results = stats_ols.run_ols_regression(
    csv_path=csv_path, target=target, predictors=features
)

# Print results
print("✅ Regression complete. Summary:\n")
print(results.summary())

# Save residuals plot
output_path = OUTPUT_DIR / "OLS_Regression_Residuals_vs_Fitted_Values.png"
stats_ols.plot_residuals(df, results, output_path=output_path)
print(f"\n🖼️ Residuals plot saved to: {output_path}")
