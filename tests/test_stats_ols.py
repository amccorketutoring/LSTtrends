import unittest
from pathlib import Path
import pandas as pd
from lsttrends.analysis import stats_ols
from lsttrends.analysis import preprocessing

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent / "data"
csv_path = DATA_DIR / "Knox_UHI_Zonal_Stats_STRM.csv"
required_exists = csv_path.exists()

@unittest.skipUnless(required_exists, "Required CSV file not found.")
class TestOLSRegression(unittest.TestCase):
    def test_ols_regression_output(self):
        df = preprocessing.load_and_clean_data(csv_path)
        features = ["NDVI", "BuildingDensity", "Slope", "Aspect"]
        target = "LST_Celsius"
        model, results = stats_ols.run_ols_regression(df, target=target, predictors=features)
        self.assertTrue("R-squared" in results.summary().as_text())

    def test_plot_residuals(self):
        df = preprocessing.load_and_clean_data(csv_path)
        features = ["NDVI", "BuildingDensity", "Slope", "Aspect"]
        target = "LST_Celsius"
        _, results = stats_ols.run_ols_regression(df, target=target, predictors=features)
        output_path = HERE.parent / "outputs" / "OLS_Residuals_Test.png"
        stats_ols.plot_residuals(df, results, output_path=output_path)
        self.assertTrue(output_path.exists())

if __name__ == "__main__":
    unittest.main()
