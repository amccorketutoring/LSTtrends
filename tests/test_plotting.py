# tests/test_plotting.py

import unittest
from pathlib import Path
from lsttrends.analysis import preprocessing
from lsttrends.visualization import plotting

DATA_PATH = Path("data/Knox_UHI_Zonal_Stats_STRM.csv")


@unittest.skipIf(
    not DATA_PATH.exists(),
    "Required CSV file is missing: Knox_UHI_Zonal_Stats_STRM.csv",
)
class TestRadarChart(unittest.TestCase):
    def test_plot_radar_chart(self):
        # Load and clean the data
        df = preprocessing.load_and_clean_data(DATA_PATH)
        features = ["LST_Celsius", "NDVI", "BuildingDensity", "Slope", "Aspect"]

        # Normalize
        df_scaled, _ = preprocessing.normalize_columns(df, features)
        df_scaled["Cluster"] = 0  # Dummy cluster assignment for one cluster

        # Simulate cluster means
        cluster_means = df_scaled.groupby("Cluster")[features].mean()

        # Define color palette
        colors = ["r"]

        # Plot and save radar chart
        plotting.plot_radar_chart(
            cluster_means, features, colors, output_path="outputs/test_radar_chart.png"
        )


if __name__ == "__main__":
    unittest.main()
