// FINAL PROJECT CODE (30-Year UHI Study - Knox County, TN)
// Version 3 + Enhancements from Version 2

// 1. Define Study Area (Knox County, TN) ***
var counties = ee.FeatureCollection("TIGER/2018/Counties");
var knox = counties.filter(ee.Filter.eq('NAME', 'Knox'))
                   .filter(ee.Filter.eq('STATEFP', '47'))
                   .first();
var knoxGeometry = knox.geometry();
Map.centerObject(knox, 9);

// --- Dynamic Legend Function ---
function createLegend(title, palette, min, max) {
  var legend = ui.Panel({
    style: { position: 'bottom-left', padding: '8px 15px' }
  });

  var titleLabel = ui.Label({
    value: title,
    style: {fontWeight: 'bold', fontSize: '16px', margin: '0 0 4px 0', padding: '0'}
  });

  var makeColorBar = function(palette) {
    return ui.Thumbnail({
      image: ee.Image.pixelLonLat().select(0)
        .multiply((max - min) / 100.0)
        .add(min)
        .visualize({min: min, max: max, palette: palette}),
      params: {bbox: [0, 0, 100, 10], dimensions: '100x10'},
      style: {stretch: 'horizontal', margin: '0px 8px', maxHeight: '24px'}
    });
  };

  var minLabel = ui.Label(min, {margin: '4px 8px'});
  var maxLabel = ui.Label(max, {margin: '4px 8px', textAlign: 'right', stretch: 'horizontal'});

  legend.add(titleLabel);
  legend.add(makeColorBar(palette));
  legend.add(ui.Panel([minLabel, maxLabel], ui.Panel.Layout.flow('horizontal')));

  Map.add(legend);
}

// 2. Define Analysis Parameters
var startYear = 1995;
var endYear = 2024;

// 3. Load and Prepare Satellite Data
function maskCloudsLandsat(img) {
  var qa = img.select('QA_PIXEL');
  var cloudMask = qa.bitwiseAnd(1 << 3).eq(0).and(qa.bitwiseAnd(1 << 5).eq(0));
  return img.updateMask(cloudMask);
}

function addLST_NDVI_L57(img) {
  img = maskCloudsLandsat(img);
  var lst = img.select('ST_B6').multiply(0.00341802).add(149.0).subtract(273.15).rename('LST');
  var red = img.select('SR_B3').multiply(0.0000275).add(-0.2);
  var nir = img.select('SR_B4').multiply(0.0000275).add(-0.2);
  var ndvi = nir.subtract(red).divide(nir.add(red)).rename('NDVI');
  return img.addBands(lst).addBands(ndvi);
}

function addLST_NDVI_L89(img) {
  img = maskCloudsLandsat(img);
  var lst = img.select('ST_B10').multiply(0.00341802).add(149.0).subtract(273.15).rename('LST');
  var red = img.select('SR_B4').multiply(0.0000275).add(-0.2);
  var nir = img.select('SR_B5').multiply(0.0000275).add(-0.2);
  var ndvi = nir.subtract(red).divide(nir.add(red)).rename('NDVI');
  return img.addBands(lst).addBands(ndvi);
}

var l5Coll = ee.ImageCollection("LANDSAT/LT05/C02/T1_L2")
  .filterDate('1995-01-01', '2011-12-31')
  .filterBounds(knoxGeometry)
  .map(addLST_NDVI_L57);

var l7Coll = ee.ImageCollection("LANDSAT/LE07/C02/T1_L2")
  .filterDate('1999-01-01', '2024-12-31')
  .filterBounds(knoxGeometry)
  .map(addLST_NDVI_L57);

var l8Coll = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
  .filterDate('2013-01-01', '2024-12-31')
  .filterBounds(knoxGeometry)
  .map(addLST_NDVI_L89);

var l9Coll = ee.ImageCollection("LANDSAT/LC09/C02/T1_L2")
  .filterDate('2022-01-01', '2024-12-31')
  .filterBounds(knoxGeometry)
  .map(addLST_NDVI_L89);

var allLandsat = l5Coll.merge(l7Coll).merge(l8Coll).merge(l9Coll);

// Load Supporting Data Layers
var built1990 = ee.Image('JRC/GHSL/P2023A/GHS_BUILT_S/1990').select('built_surface').clip(knoxGeometry);
var built2020 = ee.Image('JRC/GHSL/P2023A/GHS_BUILT_S/2020').select('built_surface').clip(knoxGeometry);
var builtChange = built2020.subtract(built1990);

var bldgHeight = ee.ImageCollection("JRC/GHSL/P2023A/GHS_BUILT_H")
  .filterDate('2018-01-01', '2019-01-01')
  .first()
  .select('built_height')
  .clip(knoxGeometry);

// Visualization Layers
var lstVis = {
  min: 0,
  max: 40,
  palette: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
};
var ndviVis = {
  min: 0,
  max: 1,
  palette: ['#ffffe5', '#f7fcb9', '#d9f0a3', '#addd8e', '#78c679', '#41ab5d', '#238443', '#006837']
};
var heightVis = {
  min: 0,
  max: 50,
  palette: ['#000004', '#1b0c41', '#4a0c6b', '#781c6d', '#a52c60', '#cf4446', '#ed6925', '#fb9b06', '#f7d13d', '#fcffa4']
};
var builtChangeVis = {
  min: 0,
  max: 2000,
  palette: ['#ffffff', '#fee8c8', '#fdbb84', '#fc8d59', '#ef6548', '#d7301f', '#990000']
};

var summer2020 = allLandsat.filterDate('2020-06-01', '2020-09-01').select('LST').mean().clip(knoxGeometry);
var summerNDVI = allLandsat.filterDate('2020-06-01', '2020-09-01').select('NDVI').mean().clip(knoxGeometry);

Map.addLayer(builtChange, builtChangeVis, 'Built-up Change 1990-2020');
createLegend('Built-up Change', builtChangeVis.palette, builtChangeVis.min, builtChangeVis.max);

Map.addLayer(summer2020, lstVis, 'Mean Summer LST (1995-2024)');
createLegend('Summer LST (°C)', lstVis.palette, lstVis.min, lstVis.max);

Map.addLayer(summerNDVI, ndviVis, 'Mean Summer NDVI (1995–2024)');
createLegend('Summer NDVI', ndviVis.palette, ndviVis.min, ndviVis.max);

Map.addLayer(bldgHeight, heightVis, 'Building Height (m)');
createLegend('Building Height (m)', heightVis.palette, heightVis.min, heightVis.max);

// Add Buildings and Roads Layers
var buildings = ee.FeatureCollection("projects/our-lacing-276422/assets/KnoxCountyBorder")
  .filterBounds(knoxGeometry);
Map.addLayer(buildings, {color: 'gray'}, 'Buildings');

var roads = ee.FeatureCollection("projects/our-lacing-276422/assets/TNRoads");
Map.addLayer(roads, {color: 'white'}, 'Roads');

// 6. Animations

// Built-up Growth Animation 1990-2020
var builtYears = ['1990', '2000', '2015', '2020'];
var builtCollection = ee.ImageCollection(
  builtYears.map(function(year) {
    return ee.Image('JRC/GHSL/P2023A/GHS_BUILT_S/' + year)
      .select('built_surface')
      .clip(knoxGeometry)
      .set('year', year);
  })
);

var builtVisParams = {
  min: 0,
  max: 8000,
  palette: ['#ffffff', '#cccccc', '#888888', '#444444', '#000000']
};

var builtFrames = builtCollection.map(function(img) {
  return img.visualize(builtVisParams)
    .set('label', img.get('year'));
});

Export.video.toDrive({
  collection: builtFrames,
  description: 'Knox_Builtup_Growth_1990_2020',
  fileNamePrefix: 'Knox_BuiltupGrowth',
  framesPerSecond: 1,
  dimensions: 720,
  region: knoxGeometry,
  crs: 'EPSG:4326'
});

// Summer LST Progression Animation 1995-2024
var summerYears = ee.List.sequence(startYear, endYear);
var summerLSTCollection = ee.ImageCollection(summerYears.map(function(year) {
  var summer = allLandsat.filterDate(
    ee.Date.fromYMD(year, 6, 1),
    ee.Date.fromYMD(year, 9, 1)
  ).select('LST')
   .mean()
   .clip(knoxGeometry)
   .set('year', year);

  return summer.visualize({
    min: 0,
    max: 40,
    palette: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
  }).set('label', ee.Number(year).format());
}));

Export.video.toDrive({
  collection: summerLSTCollection,
  description: 'Knox_Summer_LST_Progression',
  fileNamePrefix: 'Knox_Summer_LST',
  framesPerSecond: 2,
  dimensions: 720,
  region: knoxGeometry,
  crs: 'EPSG:4326'
});

// *** 7. Prepare Terrain Variables, Building Density, and Summer Mean 1995-2024 ***

// Load Copernicus DEM and Calculate Slope and Aspect
var dem = ee.Image("USGS/SRTMGL1_003")
  .select('elevation')
  .clip(knoxGeometry);

var slope = ee.Terrain.slope(dem);
var aspect = ee.Terrain.aspect(dem);

// Building Density from Built-up 2020 (GHSL)
var buildingDensity = built2020.divide(100).rename('BuildingDensity');

// Calculate Mean Summer NDVI and LST across 1995-2024
var summerAllYears = allLandsat
  .filter(ee.Filter.calendarRange(6, 8, 'month'))  // June to August
  .select(['LST', 'NDVI'])
  .mean()
  .clip(knoxGeometry);

var summerAvgLST = summerAllYears.select('LST');
var summerAvgNDVI = summerAllYears.select('NDVI');

// *** 8. Zonal Statistics Calculation ***

// Create 1000m Grid Over Knox County
var scale = 1000;
var bounds = knoxGeometry.bounds();
var grid = ee.FeatureCollection(bounds.coveringGrid('EPSG:4326', scale));

// Add Centroid Coordinates (Latitude and Longitude) to each Grid Cell
grid = grid.map(function(feature) {
  var centroid = feature.geometry().centroid(ee.ErrorMargin(1));
  var lon = centroid.coordinates().get(0);
  var lat = centroid.coordinates().get(1);
  return feature.set({
    'longitude': lon,
    'latitude': lat
  });
});

// Clip grid tightly to Knox County boundary
grid = grid.map(function(feature) {
  return feature.intersection(knoxGeometry, ee.ErrorMargin(1));
});

// Visualize the Grid
Map.addLayer(
  grid.style({color: 'blue', width: 1}),
  {},
  'Grid Zones'
);

// Define Zonal Statistics Function
var zonalStats = function(feature) {
  var lst = summerAvgLST.reduceRegion({
    reducer: ee.Reducer.mean(),
    geometry: feature.geometry(),
    scale: 30,
    maxPixels: 1e9
  }).get('LST');

  var ndviVal = summerAvgNDVI.reduceRegion({
    reducer: ee.Reducer.mean(),
    geometry: feature.geometry(),
    scale: 30,
    maxPixels: 1e9
  }).get('NDVI');

  var densityVal = buildingDensity.reduceRegion({
    reducer: ee.Reducer.mean(),
    geometry: feature.geometry(),
    scale: 30,
    maxPixels: 1e9
  }).get('BuildingDensity');

  var slopeVal = slope.reduceRegion({
    reducer: ee.Reducer.mean(),
    geometry: feature.geometry(),
    scale: 30,
    maxPixels: 1e9
  }).get('slope');

  var aspectVal = aspect.reduceRegion({
    reducer: ee.Reducer.mean(),
    geometry: feature.geometry(),
    scale: 30,
    maxPixels: 1e9
  }).get('aspect');

  return feature.set({
    'LST_Celsius': lst,
    'NDVI': ndviVal,
    'BuildingDensity': densityVal,
    'Slope': slopeVal,
    'Aspect': aspectVal
  });
};

// Apply Zonal Statistics to Grid
var stats = grid.map(function(feature) {
  return zonalStats(feature).set('GridID', feature.id());
});

// Export Zonal Statistics to Drive
Export.table.toDrive({
  collection: stats,
  description: 'Knoxville_UHI_Zonal_Stats',
  fileNamePrefix: 'Knox_UHI_Zonal_Stats',
  fileFormat: 'CSV',
  selectors: ['GridID', 'latitude', 'longitude', 'LST_Celsius', 'NDVI', 'BuildingDensity', 'Slope', 'Aspect']
});