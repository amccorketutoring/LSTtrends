# Integrating Google Earth Engine (GEE) with LSTtrends

This guide describes how to use Google Earth Engine (GEE) in combination with the `lsttrends` Python package to process satellite imagery, derive Land Surface Temperature (LST), and export data for further analysis in Python.

---

## 🔗 Earth Engine Script

You can view and run the final Earth Engine script used in this project here:

👉 [Open in Earth Engine Code Editor](https://code.earthengine.google.com/04423d46f923da2eab50d1398a490ae0)

---

## 📌 Overview of the GEE Workflow

1. **Define Study Area**
   - Uses TIGER or GAUL boundaries to isolate Knox County, Tennessee.
2. **Load Landsat Collection (1995–2024)**
   - Combines Landsat 5, 7, 8, and 9 for consistent thermal measurements.
3. **Apply Cloud Masking and Compute LST**
   - Converts thermal bands to LST in Celsius using radiance formulas.
4. **Compute Urban Morphology Indicators**
   - Includes NDVI, building density, slope, aspect using DEMs and GHSL layers.
5. **Export Zonal Statistics**
   - Aggregates and exports CSV data (e.g., `Knox_UHI_Zonal_Stats_STRM.csv`) for use in the `lsttrends` Python package.

---

## ⬇️ Exported Files

From GEE, you should export the following:
- **`Knox_UHI_Zonal_Stats_STRM.csv`** – The main zonal statistics file containing:
  - `LST_Celsius`, `NDVI`, `BuildingDensity`, `Slope`, `Aspect`, `latitude`, `longitude`
- Optional: raster layers of NDVI, building height, or LST for visualization

---

## 🐍 Analyzing with lsttrends

Once exported, place the CSV in your project’s `/data/` folder, then use the package modules like so:

```python
from lsttrends.analysis import preprocessing, stats_ols

# Load and clean GEE-exported data
df = preprocessing.load_and_clean_data("data/Knox_UHI_Zonal_Stats_STRM.csv")

# Run a regression
features = ['NDVI', 'BuildingDensity', 'Slope', 'Aspect']
target = 'LST_Celsius'
model, results = stats_ols.run_ols_regression(df, target=target, predictors=features)
print(results.summary())
```

---

## 📘 Notes
- Ensure you reproject to a proper metric CRS in GEE when computing terrain.
- Use `Export.table.toDrive()` in Earth Engine to download CSVs.
- This package assumes all spatial stats (e.g., slope, aspect) are precomputed before analysis.

---

## 🛰️ Why Use GEE + Python?

Using GEE allows you to access and process large-scale satellite data efficiently in the cloud, while `lsttrends` lets you perform localized, reproducible, and customizable analysis in Python.

