# lsttrends/__main__.py

import pandas as pd
from .summer_trend import compute_summer_lst_trend

if __name__ == "__main__":
    df = pd.DataFrame({
        "year": [2000, 2005, 2010, 2015, 2020],
        "lst": [30.2, 31.0, 32.1, 32.8, 34.0]
    })

    trend = compute_summer_lst_trend(df)
    print(f"Sanity check — sample trend: {trend:.2f} °C/decade")
