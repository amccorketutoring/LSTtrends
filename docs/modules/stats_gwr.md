# `stats_gwr` Module

This module implements **Geographically Weighted Regression (GWR)** for analyzing spatial variations in the relationship between Land Surface Temperature (LST) and urban morphology variables in Knox County, TN.

---

## 🔍 Purpose

The goal of this module is to model the **local (spatially varying) relationships** between LST and predictors such as NDVI, building density, slope, and aspect using the `mgwr` package.

---

## 🧮 Key Functions

### `run_gwr_model(save_plot=True, output_path=None)`

Performs GWR modeling using preprocessed zonal statistics and spatial coordinates.

#### Parameters:
- `save_plot` (`bool`): Whether to save the local R² map as a PNG. Default is `True`.
- `output_path` (`Path or str`): Optional path to save the output image. Defaults to `"outputs/GWR_Local_R2.png"`.

#### Returns:
- A fitted `mgwr.gwr.GWRResults` object.

---

## 📈 Output Details

### `results.summary()`
Provides detailed model outputs, including:
- **Optimal bandwidth**: Controls the neighborhood size for local modeling.
- **Local R² values**: Indicates model fit quality per location.
- **Parameter estimates**: Shows how coefficients vary spatially.
- **Residual statistics**: Helps assess model adequacy.

---

## 🗺️ Visual Output

If `save_plot=True`, the module generates a thematic map showing `local_R2` values:
- Higher `R²` values suggest strong local influence of predictors on LST.
- This map helps identify areas where urban morphology strongly explains LST variations.

---

## 🧪 Usage Example

```python
from lsttrends.analysis import GWR_KnoxCounty_UHI_Model

results = GWR_KnoxCounty_UHI_Model.run_gwr_model(save_plot=True, output_path="outputs/GWR_Test_Map.png")
print(results.summary())
```

---

## 📂 Input Requirements

- CSV file: `"data/Knox_UHI_Zonal_Stats_STRM.csv"`
    - Must include columns: `latitude`, `longitude`, `LST_Celsius`, `NDVI`, `BuildingDensity`, `Slope`, `Aspect`

---

## 🧰 Dependencies

- `mgwr`
- `geopandas`
- `shapely`
- `matplotlib`
- `sklearn`