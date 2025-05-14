from pathlib import Path
import unittest
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from lsttrends.analysis import spatial_analysis

# Load data path
HERE = Path(__file__).resolve().parent
DATA_PATH = HERE.parent / "data" / "Knox_UHI_Zonal_Stats_STRM.csv"

@unittest.skipUnless(DATA_PATH.exists(), "Required CSV file not found for spatial analysis test.")
def test_spatial_analysis():
    # Convert to GeoDataFrame with Point geometries
    df = pd.read_csv(DATA_PATH)
    geometry = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry)
    gdf.set_crs(epsg=4326, inplace=True)

    # Run Moran's I
    print("▶️ Running Moran's I spatial autocorrelation test...")
    moran = spatial_analysis.compute_morans_I(gdf, variable="LST_Celsius")

    # Output results
    print(f"Observed Moran's I: {moran.I:.4f}")
    print(f"P-value: {moran.p_sim:.4f}")

    # Optional: Save histogram plot
    OUTPUT_PATH = HERE.parent / "outputs" / "Morans_I_Simulation_Distribution.png"
    spatial_analysis.plot_morans_I_simulation(moran, output_path=OUTPUT_PATH)
    print(f"📊 Histogram saved to: {OUTPUT_PATH}")
