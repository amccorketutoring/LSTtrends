# Preprocessing data example.

## This example demonstrates how to load and prepare LST-related data using the preprocessing module.

``` python
from lsttrends.analysis import preprocessing
from pathlib import Path

# Define path to CSV
csv_path = Path("data/Knox_UHI_Zonal_Stats_STRM.csv")

# Load and clean the dataset
df = preprocessing.load_and_clean_data(csv_path)

# Normalize columns
features = ['LST_Celsius', 'NDVI', 'BuildingDensity', 'Slope', 'Aspect']
df_scaled, scaler = preprocessing.normalize_columns(df, features)

print(df_scaled.head())
```
