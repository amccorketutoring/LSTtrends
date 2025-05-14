# Clustering Module: Cluster_Radar_Chart_Knox_Exporting

This module provides functionality for generating radar charts from normalized urban morphology and LST variables. It enables quick visualization of how clustered zones differ across key features.

## Function: `generate_cluster_radar_chart`

### Description:
Generates a radar chart representing average values of features (e.g., LST, NDVI, Slope) across clusters. This is useful for profiling heat vulnerability based on urban morphology.

### Parameters:
- `csv_path` (str or Path, optional): Path to the input CSV file. If not provided, it defaults to `data/Knox_UHI_Zonal_Stats_STRM.csv`.
- `output_path` (str or Path, optional): Path to save the radar chart image. If not provided, it defaults to `outputs/Knox_Cluster_Radar_Chart.png`.

### Returns:
- None (saves radar chart to file).

### Usage Example:

```python
from lsttrends.analysis import Cluster_Radar_Chart_Knox_Exporting

# Generate radar chart with default data path and save location
Cluster_Radar_Chart_Knox_Exporting.generate_cluster_radar_chart()
```