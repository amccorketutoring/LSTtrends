# Clustering Radar Chart Example

## This example generates a radar chart of cluster means for LST and urban morphology features.

```python
from lsttrends.analysis import clustering
from pathlib import Path

output_path = Path("outputs/Knox_Cluster_Radar_Chart.png")
clustering.generate_cluster_radar_chart(output_path=output_path)
```