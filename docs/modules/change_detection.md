# Change Detection Module

This module performs change detection between two built-up surface rasters (e.g., from 1990 and 2020) and produces a static visualization of the changes across the study area.

## Purpose

It helps detect how the spatial footprint of urban development has evolved over time.

## Module: `ChangeDetection_BuiltUp_Knox.py`

### Key Features

- Loads two raster GeoTIFFs (`Built_Surface_1990.tif`, `Built_Surface_2020.tif`)
- Handles nodata values and ensures alignment
- Computes the **difference raster** (`2020 - 1990`)
- Generates a **color-coded change map**
- Saves the output PNG figure to the `outputs/` directory

### Example Usage

```python
# Already handled within the script
python lsttrends/analysis/ChangeDetection_BuiltUp_Knox.py
```