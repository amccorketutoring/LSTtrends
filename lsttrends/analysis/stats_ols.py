"""
OLS regression module for LSTtrends.
"""

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent / "data"


def run_ols_regression(csv_path=None, target="LST_Celsius", predictors=None):
    """
    Run OLS regression on the specified target and predictor variables.

    Parameters:
    - csv_path: Optional path to CSV. Defaults to Knox County file.
    - target: Column name of the dependent variable (default: 'LST_Celsius').
    - predictors: List of column names to use as independent variables.

    Returns:
    - model: Fitted OLS model object
    - results: Model summary results
    """
    if csv_path is None:
        csv_path = DATA_DIR / "Knox_UHI_Zonal_Stats_STRM.csv"

    if predictors is None:
        predictors = ["NDVI", "BuildingDensity", "Slope", "Aspect"]

    df = pd.read_csv(csv_path)
    df = df.dropna(subset=[target] + predictors)

    X = df[predictors]
    X = sm.add_constant(X)
    y = df[target]

    model = sm.OLS(y, X)
    results = model.fit()
    return model, results


def plot_residuals(df, results, output_path=None):
    """Plot residuals vs fitted values."""
    fitted_vals = results.fittedvalues
    residuals = results.resid

    plt.figure(figsize=(8, 6))
    plt.scatter(fitted_vals, residuals, alpha=0.5)
    plt.axhline(0, color="red", linestyle="--")
    plt.xlabel("Fitted Values")
    plt.ylabel("Residuals")
    plt.title("Residuals vs Fitted Values")

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=300)
        print(f"✅ Residual plot saved to: {output_path}")
        plt.close()
    else:
        plt.show()
