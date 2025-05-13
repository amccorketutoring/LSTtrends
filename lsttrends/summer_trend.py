import geopandas as gpd
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# Define data path relative to this file
HERE = Path(__file__).parent
DATA_DIR = HERE.parent / "data"


def load_vector_data(filename: str) -> gpd.GeoDataFrame:
    """
    Load a GeoJSON or Shapefile from the data directory.

    Args:
        filename (str): Filename located in the /data directory.

    Returns:
        gpd.GeoDataFrame: Loaded vector data.
    """
    filepath = DATA_DIR / filename
    return gpd.read_file(filepath)


def compute_summer_lst_trend(df: pd.DataFrame, year_col="year", lst_col="lst") -> float:
    """
    Compute the linear trend (slope) of summer LST over time using linear regression.

    Args:
        df (pd.DataFrame): DataFrame with columns for year and LST.
        year_col (str): Column name for the year.
        lst_col (str): Column name for land surface temperature values.

    Returns:
        float: Slope (°C/year) of the trend.
    """
    if year_col not in df.columns or lst_col not in df.columns:
        raise ValueError(
            f"Columns '{year_col}' and/or '{lst_col}' not found in DataFrame."
        )

    x = df[year_col].to_numpy()
    y = df[lst_col].to_numpy()

    # Remove NaNs
    mask = ~np.isnan(x) & ~np.isnan(y)
    x, y = x[mask], y[mask]

    # Linear regression: slope
    slope, _ = np.polyfit(x, y, 1)
    return slope


def plot_trend(df: pd.DataFrame, year_col="year", lst_col="lst", title="LST Trend"):
    """
    Plot the LST time series with a trend line.

    Args:
        df (pd.DataFrame): DataFrame with year and LST columns.
        year_col (str): Column for year.
        lst_col (str): Column for LST.
        title (str): Plot title.
    """
    x = df[year_col]
    y = df[lst_col]
    slope, intercept = np.polyfit(x, y, 1)
    trend_line = slope * x + intercept

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, "o", label="Observed LST")
    plt.plot(x, trend_line, "-", color="red", label=f"Trend: {slope:.2f} °C/year")
    plt.xlabel("Year")
    plt.ylabel("LST (°C)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
