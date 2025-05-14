# Moran's I Example

## This example computes Moran's I statistic and visualizes the spatial autocorrelation.

``` python
from lsttrends.analysis import spatial_analysis
from pathlib import Path
import geopandas as gpd

gdf = spatial_analysis.load_geodataframe()
moran = spatial_analysis.compute_morans_I(gdf, variable="LST_Celsius")

# Plot simulation histogram
spatial_analysis.plot_morans_I_simulation(moran, output_path=Path("outputs/Morans_I_Simulation_Distribution.png"))

# Print result
print(f"Moran's I: {moran.I:.4f}, p-value: {moran.p_sim:.4f}")
```