## GEE LST Example

## This script fetches a summer Landsat 8 image over Knoxville, converts the thermal band to Celsius, and displays the LST values on the map.

This example demonstrates how Land Surface Temperature (LST) can be calculated using Landsat thermal bands and visualized for a defined area using GEE JavaScript.

```javascript
// Load a Landsat image (example: Landsat 8)
var image = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
  .filterBounds(ee.Geometry.Point([-83.9207, 35.9606]))  // Knoxville, TN
  .filterDate("2020-07-01", "2020-08-31")
  .sort("CLOUD_COVER")
  .first();

// Convert thermal band to LST (Kelvin to Celsius)
var lst = image.select("ST_B10")
               .multiply(0.00341802)
               .add(149.0)
               .subtract(273.15)
               .rename("LST_C");

// Center and visualize
Map.centerObject(image, 10);
Map.addLayer(lst, {min: 20, max: 45, palette: ["blue", "yellow", "red"]}, "LST (°C)");
```

## This is not the the GEE script that this project is based on. It's just an example of how to use GEE to calculate LST.