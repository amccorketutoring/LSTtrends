# Preprocessing Module

This module contains functions used for loading, cleaning, and preparing zonal statistics data for analysis.

## Functions

### `load_zonal_stats(csv_path)`
Loads a CSV file containing zonal statistics data.

**Parameters:**
- `csv_path` (str or Path): Path to the CSV file.

**Returns:**
- `pandas.DataFrame`: Loaded dataset.

---

### `drop_na(df, columns)`
Drops rows from the DataFrame that contain NA values in specified columns.

**Parameters:**
- `df` (pandas.DataFrame): Input DataFrame.
- `columns` (list): List of column names to check for NA.

**Returns:**
- `pandas.DataFrame`: Cleaned DataFrame without NA in specified columns.

---

### `normalize_columns(df, columns, scaler=None)`
Normalizes the values in selected columns using MinMaxScaler or a provided scaler.

**Parameters:**
- `df` (pandas.DataFrame): Input DataFrame.
- `columns` (list): List of column names to normalize.
- `scaler` (object, optional): Custom scaler. Default is `MinMaxScaler`.

**Returns:**
- `pandas.DataFrame`: DataFrame with normalized values.
- `scaler`: The scaler object used.

---

### `load_and_clean_data(csv_path)`
Wrapper function that loads a CSV and removes rows with missing values in key analysis columns.

**Parameters:**
- `csv_path` (str or Path): Path to the CSV file.

**Returns:**
- `pandas.DataFrame`: Cleaned dataset with key features prepared for analysis.

---

## Usage Example

```python
from lsttrends.analysis import preprocessing

df = preprocessing.load_and_clean_data("data/Knox_UHI_Zonal_Stats_STRM.csv")
df_scaled, scaler = preprocessing.normalize_columns(df, ['LST_Celsius', 'NDVI', 'BuildingDensity', 'Slope', 'Aspect'])
```