import unittest
from pathlib import Path
from lsttrends.analysis import clustering

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent / "data"
INPUT_FILE = DATA_DIR / "Knox_UHI_Zonal_Stats_STRM.csv"
OUTPUT_DIR = HERE.parent / "outputs"
chart_path = OUTPUT_DIR / "Knox_Cluster_Radar_Chart_Test.png"


@unittest.skipUnless(INPUT_FILE.exists(), "Knox_UHI_Zonal_Stats_STRM.csv is missing")
class TestClustering(unittest.TestCase):
    def test_generate_cluster_chart(self):
        """Test radar chart generation for clustering module."""
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        print("▶️ Generating cluster radar chart...")
        clustering.generate_cluster_radar_chart(output_path=chart_path)

        # Check if file was created
        self.assertTrue(chart_path.exists(), "❌ Cluster radar chart was not created.")
        if chart_path.exists():
            print(f"✅ Cluster radar chart successfully generated at: {chart_path}")
