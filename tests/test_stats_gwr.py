from pathlib import Path
from lsttrends.analysis import stats_gwr

# Define path to save the plot
HERE = Path(__file__).resolve().parent
OUTPUT_DIR = HERE.parent / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
output_path = OUTPUT_DIR / "GWR_Local_R2_Test.png"

# Run the GWR model
print("Running Geographically Weighted Regression (GWR)...")
results = stats_gwr.run_gwr_model(save_plot=True, output_path=output_path)

# Print summary
print("\n✅ GWR model run successfully.\n")
print(results.summary())
print(f"\n🖼️  Local R² map saved to: {output_path}")
