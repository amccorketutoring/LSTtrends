# `spatial_analysis` - Spatial Autocorrelation Tools

This module provides spatial statistics tools for analyzing spatial patterns in urban heat island (UHI) studies. It currently supports Moran's I calculation and histogram visualization for evaluating spatial autocorrelation in LST (Land Surface Temperature) or other spatial variables.

## Functions

### `compute_morans_I(df, variable='LST_Celsius')`

**Description**:
Computes Moran's I statistic using a Queen contiguity spatial weights matrix.

**Parameters**:
- `df` (*GeoDataFrame*): A geopandas dataframe with geometry and the target variable.
- `variable` (*str*): The column name for the variable to test (default: `'LST_Celsius'`).

**Returns**:
- `esda.Moran`: A Moran object containing I statistic, p-value, and simulation data.

---

### `plot_morans_I_simulation(moran, output_path=None)`

**Description**:
Plots the histogram of simulated Moran's I values, with the observed value marked by a red dashed line.

**Parameters**:
- `moran` (*esda.Moran*): The Moran object returned from `compute_morans_I()`.
- `output_path` (*Path or str*, optional): If provided, saves the plot to the given file path.

---

## Usage Example

```python
from lsttrends.analysis import spatial_analysis
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

# Load your data
df = pd.read_csv("data/Knox_UHI_Zonal_Stats_STRM.csv")
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry)
gdf.set_crs(epsg=4326, inplace=True)

# Compute Moran's I
moran = spatial_analysis.compute_morans_I(gdf, variable='LST_Celsius')
print(moran.I, moran.p_sim)

# Plot
spatial_analysis.plot_morans_I_simulation(moran, output_path="outputs/Morans_I_Simulation.png")
```