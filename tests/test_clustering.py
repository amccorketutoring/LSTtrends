from pathlib import Path
from lsttrends.analysis import clustering

# Define output path for the radar chart
HERE = Path(__file__).resolve().parent
OUTPUT_DIR = HERE.parent / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

chart_path = OUTPUT_DIR / "Knox_Cluster_Radar_Chart_Test.png"

# Run the cluster radar chart generator
print("▶️ Generating cluster radar chart...")
clustering.generate_cluster_radar_chart(output_path=chart_path)

# Confirm chart was saved
if chart_path.exists():
    print(f"✅ Cluster radar chart successfully generated at: {chart_path}")
else:
    print("❌ Chart generation failed.")
