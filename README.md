# LSTtrends

<p align="center">
  <img src="docs/assets/logo.png" alt="LSTtrends logo" width="250"/>
</p>

<h1 align="center">LSTtrends</h1>

<p align="center">
  Analyze long-term summer Land Surface Temperature (LST) trends, urban morphology, and heat vulnerability using Google Earth Engine and Python.
</p>

<p align="center">
  <a href="https://pypi.org/project/lsttrends">
    <img src="https://img.shields.io/pypi/v/lsttrends.svg" alt="PyPI">
  </a>
  <a href="https://anaconda.org/conda-forge/lsttrends">
    <img src="https://img.shields.io/conda/vn/conda-forge/lsttrends.svg" alt="Conda">
  </a>
  <a href="https://github.com/amccorketutoring/lsttrends/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/amccorketutoring/lsttrends.svg" alt="License">
  </a>
  <a href="https://pypi.org/project/lsttrends">
    <img src="https://img.shields.io/pypi/pyversions/lsttrends.svg" alt="Python">
  </a>
</p>

---

## 🔥 Overview

`LSTtrends` is a geospatial analysis toolkit to:

- Analyze long-term LST trends from Landsat imagery
- Run statistical models (OLS, GWR) on urban heat metrics
- Detect changes in built-up surface area
- Evaluate spatial autocorrelation (Moran’s I)
- Visualize vulnerability using multi-factor indices
- Integrate Google Earth Engine for remote sensing workflows

---

## 📦 Installation

Install with pip:

```bash
pip install lsttrends
```

Install optional dependencies:

```bash
pip install lsttrends[viz,spatial,gee]
```

---

## ⚙️ CLI Usage

```bash
python -m lsttrends.cli --check
python -m lsttrends.cli path/to/your_data.csv
```

---

## 🧠 Example of Modules (UHI Vulnerability)

This example visualizes urban heat vulnerability using normalized factors.

``` python
from lsttrends.analysis import uhi_vulnerability
from pathlib import Path

uhi_vulnerability.generate_vulnerability_map(output_path=Path("outputs/UHI_Vulnerability_Map.png"))
```

More examples for each module are available in the [`examples/`](docs/examples/) folder and at the [📘 documentation site](https://amccorketutoring.github.io/lsttrends/).

---

## 📁 Project Structure

```text
LSTtrends/
├── data/ # Input CSVs, TIFFs, shapefiles
├── docs/ # Documentation (MkDocs-based)
│ ├── assets/ # Static assets (e.g., logo)
│ ├── modules/ # Module documentation files (.md)
│ ├── examples/ # Code usage examples
│ └── index.md # Homepage for documentation
├── examples/ # Standalone .md usage examples
├── lsttrends/ # Python package source code
│ ├── init.py
│ ├── main.py
│ ├── cli.py
│ ├── common.py
│ ├── summer_trend.py
│ ├── analysis/ # All analysis modules
│ │ ├── preprocessing.py
│ │ ├── stats_ols.py
│ │ ├── stats_gwr.py
│ │ ├── spatial_analysis.py
│ │ ├── clustering.py
│ │ ├── change_detection.py
│ │ └── uhi_vulnerability.py
│ ├── visualization/ # Plotting functions
│ │ └── plotting.py
│ └── gee/ # GEE scripts (e.g., .js)
│ └── final_uhi_code.js
├── outputs/ # Generated images, charts, maps
├── tests/ # Unit tests for each module
│ └── test_*.py
├── pyproject.toml
├── requirements.txt
├── requirements_dev.txt
├── .pre-commit-config.yaml
├── README.md
└── LICENSE
```

---

## ✅ Testing

Run tests using:

```bash
pytest tests/
```

Or use pre-commit:

```bash
pre-commit run --all-files
```

---

## 🌍 Earth Engine Integration

This package integrates with [Google Earth Engine](https://earthengine.google.com/) via:

- Preprocessed data exports (LST, NDVI, built area)
- JavaScript code stored under `lsttrends/gee`
- [➡ View the GEE Code](https://code.earthengine.google.com/04423d46f923da2eab50d1398a490ae0)

For full integration guidance, see [`docs/gee_integration.md`](docs/gee_integration.md).

---

## 📚 Documentation

📘 [https://amccorketutoring.github.io/lsttrends/](https://amccorketutoring.github.io/lsttrends/)

Includes:

- API reference
- Example visualizations
- How-to guides
- GEE integration

---

## 📄 License

MIT License — see [`LICENSE`](LICENSE)

---

## 🙌 Author

Alex McCorkel — [amccorketutoring@gmail.com](mailto:amccorketutoring@gmail.com)
