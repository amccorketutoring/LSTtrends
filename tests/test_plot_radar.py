import unittest
from pathlib import Path
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from lsttrends.analysis import clustering

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent / "data"
DEFAULT_CSV = DATA_DIR / "Knox_UHI_Zonal_Stats_STRM.csv"
TEST_OUTPUT = HERE.parent / "outputs" / "Radar_Chart_Test.png"


@unittest.skipUnless(DEFAULT_CSV.exists(), "Knox_UHI_Zonal_Stats_STRM.csv is missing")
class TestRadarPlot(unittest.TestCase):
    def test_radar_chart_generation(self):
        """Test radar chart generation and saving"""
        clustering.generate_cluster_radar_chart(
            csv_path=DEFAULT_CSV, output_path=TEST_OUTPUT
        )
        self.assertTrue(TEST_OUTPUT.exists(), "Radar chart output was not created.")
