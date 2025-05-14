import unittest
from pathlib import Path
from lsttrends.analysis import stats_gwr

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent / "data"
csv_path = DATA_DIR / "Knox_UHI_Zonal_Stats_STRM.csv"
required_exists = csv_path.exists()

@unittest.skipUnless(required_exists, "Required data file not found.")
class TestGWR(unittest.TestCase):
    def test_run_gwr_model(self):
        output_path = HERE.parent / "outputs" / "GWR_Local_R2_Test.png"
        results = stats_gwr.run_gwr_model(save_plot=True, output_path=output_path)
        self.assertTrue(hasattr(results, "localR2"))

if __name__ == "__main__":
    unittest.main()
