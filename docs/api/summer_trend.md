# `lsttrends.summer_trend` Module

This module provides core analysis functions for the `LSTtrends` package.

## Functions

### `load_vector_data(filename: str) -> gpd.GeoDataFrame`
Load a GeoJSON or Shapefile from the `/data` directory.

### `compute_summer_lst_trend(df: pd.DataFrame, year_col="year", lst_col="lst") -> float`
Compute a linear regression slope over time from annual summer LST data.

### `plot_trend(df: pd.DataFrame, year_col="year", lst_col="lst", title="LST Trend")`
Plot a time series of LST data with a fitted trend line.
