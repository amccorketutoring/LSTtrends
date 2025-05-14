import rasterio
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Define relative paths
HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent.parent / "data"
OUTPUT_DIR = HERE.parent.parent / "outputs"

INPUT_1990 = DATA_DIR / "Built_Surface_1990.tif"
INPUT_2020 = DATA_DIR / "Built_Surface_2020.tif"
OUTPUT_FIG = OUTPUT_DIR / "Built_Surface_Change_1990_to_2020.png"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load 1990 and 2020 built-up rasters
with rasterio.open(INPUT_1990) as src90:
    built90 = src90.read(1).astype(float)
    profile = src90.profile

with rasterio.open(INPUT_2020) as src20:
    built20 = src20.read(1).astype(float)

# Replace nodata values with NaN
nodata_val = profile.get("nodata")
if nodata_val is not None:
    built90[built90 == nodata_val] = np.nan
    built20[built20 == nodata_val] = np.nan

# Calculate change
change = built20 - built90

# Plot change detection
plt.figure(figsize=(10, 8))
plt.imshow(change, cmap="RdYlBu", vmin=-2000, vmax=2000)
plt.colorbar(label="Built-up Surface Change (2020 - 1990)")
plt.title("Built-up Surface Change (1990–2020)")
plt.axis("off")
plt.tight_layout()
plt.savefig(OUTPUT_FIG, dpi=300)
plt.close()
