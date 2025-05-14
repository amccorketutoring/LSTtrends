import unittest
from pathlib import Path
import pandas as pd
from lsttrends.analysis import stats_ols


class TestOLSRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Keep Path object for checking file existence
        cls.csv_path_obj = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "Knox_UHI_Zonal_Stats_STRM.csv"
        )
        cls.required_exists = cls.csv_path_obj.exists()
        cls.csv_path = str(cls.csv_path_obj)

        cls.target = "LST_Celsius"
        cls.predictors = ["NDVI", "BuildingDensity", "Slope", "Aspect"]

    @unittest.skipUnless(
        required_exists := (
            Path(__file__).resolve().parent.parent
            / "data"
            / "Knox_UHI_Zonal_Stats_STRM.csv"
        ).exists(),
        "CSV data file not found for OLS regression test.",
    )
    def test_ols_regression_output(self):
        df = pd.read_csv(self.csv_path)
        model, results = stats_ols.run_ols_regression(
            csv_path=self.csv_path, target=self.target, predictors=self.predictors
        )
        self.assertTrue(hasattr(results, "summary"))

    @unittest.skipUnless(
        required_exists := (
            Path(__file__).resolve().parent.parent
            / "data"
            / "Knox_UHI_Zonal_Stats_STRM.csv"
        ).exists(),
        "CSV data file not found for OLS residual plot test.",
    )
    def test_plot_residuals(self):
        df = pd.read_csv(self.csv_path)
        _, results = stats_ols.run_ols_regression(
            csv_path=self.csv_path, target=self.target, predictors=self.predictors
        )
        output_path = (
            Path(__file__).resolve().parent.parent
            / "outputs"
            / "OLS_Residuals_Test_Plot.png"
        )
        stats_ols.plot_residuals(df, results, output_path)
