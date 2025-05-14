"""
Preprocessing functions for LSTtrends.
Includes functions for loading, cleaning, and preparing zonal stats data.
"""

from pathlib import Path
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Define data path relative to this module
HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent.parent / "data"
DEFAULT_CSV = DATA_DIR / "Knox_UHI_Zonal_Stats_STRM.csv"


def load_zonal_stats(csv_path=DEFAULT_CSV):
    """Load the zonal statistics CSV."""
    return pd.read_csv(csv_path)


def drop_na(df, columns):
    """Drop rows with NA in selected columns."""
    return df.dropna(subset=columns)


def normalize_columns(df, columns, scaler=None):
    """Normalize selected columns using a provided scaler (e.g., MinMaxScaler)."""
    scaler = scaler or MinMaxScaler()
    df_scaled = scaler.fit_transform(df[columns])
    return pd.DataFrame(df_scaled, columns=columns), scaler


def load_and_clean_data(csv_path=DEFAULT_CSV):
    """Convenience wrapper to load CSV and drop rows with missing values."""
    df = load_zonal_stats(csv_path)
    return drop_na(df, ["LST_Celsius", "NDVI", "BuildingDensity", "Slope", "Aspect"])
