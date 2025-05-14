"""
Spatial autocorrelation functions for LSTtrends.
Includes Moran's I computation and visualization.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from esda import Moran
from libpysal.weights import Queen


def compute_morans_I(gdf, variable="LST_Celsius"):
    """Compute Moran's I statistic for a given variable using a GeoDataFrame."""
    w = Queen.from_dataframe(gdf)
    w.transform = "r"
    moran = Moran(gdf[variable], w, permutations=999)
    return moran


def plot_morans_I_simulation(moran, output_path=None):
    """Plot the histogram of simulated Moran's I with observed value."""
    if moran.sim is not None and np.isfinite(moran.sim).all():
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(moran.sim, bins=30, color="skyblue", edgecolor="black")
        ax.axvline(
            moran.I, color="red", linestyle="--", label=f"Observed I = {moran.I:.4f}"
        )
        ax.set_title("Moran's I Simulation Distribution")
        ax.set_xlabel("Simulated Moran's I")
        ax.set_ylabel("Frequency")
        ax.legend()

        if output_path:
            plt.savefig(output_path, dpi=300)
        plt.show()
