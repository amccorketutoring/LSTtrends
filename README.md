# lsttrends

[![image](https://img.shields.io/pypi/v/lsttrends.svg)](https://pypi.python.org/pypi/lsttrends)
[![image](https://img.shields.io/conda/vn/conda-forge/lsttrends.svg)](https://anaconda.org/conda-forge/lsttrends)

**Analyze summer Land Surface Temperature trends from satellite imagery**

-   Free software: MIT License
-   Documentation: https://amccorketutoring.github.io/lsttrends

---

## Installation

```bash
pip install lsttrends
```

## CLI Usage

```bash
python -m lsttrends.cli --check
python -m lsttrends.cli path/to/your_data.csv
```

Sample output:

```text
[Check] Sample data preview:
   year   lst
0  2000  30.2
1  2005  31.0
2  2010  32.1
3  2015  32.8
4  2020  34.0
[Check] Computed trend: 0.19 °C/decade
```

## Python API Usage

```python
from lsttrends.summer_trend import compute_summer_lst_trend
import pandas as pd

df = pd.DataFrame({
    "year": [2000, 2005, 2010, 2015, 2020],
    "lst": [30.2, 31.0, 32.1, 32.8, 34.0]
})

trend = compute_summer_lst_trend(df)
print(f"LST Trend: {trend:.2f} °C/decade")
```

## Project Structure

```text
lsttrends/
├── __init__.py
├── cli.py
├── common.py
├── summer_trend.py
data/
└── sample_data.csv
tests/
└── test_summer_trend.py
```

## Testing

```bash
pytest tests/
```

## Documentation

Full API and usage documentation:
👉 https://amccorketutoring.github.io/lsttrends
