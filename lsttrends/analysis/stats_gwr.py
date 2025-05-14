from pathlib import Path
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from mgwr.gwr import GWR
from mgwr.sel_bw import Sel_BW
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# Set up reusable default paths
HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent.parent / "data"
DEFAULT_CSV = DATA_DIR / "Knox_UHI_Zonal_Stats_STRM.csv"


def run_gwr_model(csv_path=None, save_plot=False, output_path=None):
    """Run GWR model on Knox County UHI data and optionally plot local R²."""

    # Use default if no path is passed
    if csv_path is None:
        csv_path = DEFAULT_CSV

    # Load and clean data
    df = pd.read_csv(csv_path)
    df = df.dropna(
        subset=[
            "latitude",
            "longitude",
            "LST_Celsius",
            "NDVI",
            "BuildingDensity",
            "Slope",
            "Aspect",
        ]
    )

    # Create GeoDataFrame
    geometry = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326").to_crs(epsg=3857)

    # Prepare variables
    coords = np.array(list(zip(gdf.geometry.x, gdf.geometry.y)))
    y = gdf[["LST_Celsius"]].values
    X = gdf[["NDVI", "BuildingDensity", "Slope", "Aspect"]].values
    X_scaled = StandardScaler().fit_transform(X)

    # Bandwidth and model
    bw = Sel_BW(coords, y, X_scaled).search()
    model = GWR(coords, y, X_scaled, bw=bw)
    results = model.fit()

    # Optional plot
    if save_plot:
        gdf["local_R2"] = results.localR2
        ax = gdf.plot(
            column="local_R2",
            cmap="viridis",
            legend=True,
            figsize=(10, 8),
            markersize=25,
        )
        ax.set_title("Local R² from GWR: LST vs Urban Morphology")
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        plt.grid(True)
        plt.tight_layout()

        if output_path is None:
            output_path = HERE.parent.parent / "outputs" / "GWR_Local_R2.png"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=300)
        plt.close()

    return results
