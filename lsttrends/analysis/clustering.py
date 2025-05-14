from pathlib import Path
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np


def generate_cluster_radar_chart(csv_path=None, output_path=None):
    """Generate a radar chart of clustering results from the zonal stats CSV."""

    HERE = Path(__file__).resolve().parent
    DATA_DIR = HERE.parent.parent / "data"
    OUTPUT_DIR = HERE.parent.parent / "outputs"

    if csv_path is None:
        csv_path = DATA_DIR / "Knox_UHI_Zonal_Stats_STRM.csv"

    if output_path is None:
        output_path = OUTPUT_DIR / "Knox_Cluster_Radar_Chart.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Load and preprocess data
    df = pd.read_csv(csv_path)
    features = ["LST_Celsius", "NDVI", "BuildingDensity", "Slope", "Aspect"]
    df_clean = df.dropna(subset=features)

    # Normalize
    scaler = MinMaxScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df_clean[features]), columns=features)
    df_scaled["Cluster"] = 0  # Dummy single-cluster

    # Group means per cluster
    cluster_means = df_scaled.groupby("Cluster")[features].mean()

    # Radar chart setup
    num_vars = len(features)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    colors = ["r"]

    for i, (index, row) in enumerate(cluster_means.iterrows()):
        values = row.tolist() + [row.tolist()[0]]
        ax.plot(angles, values, color=colors[i], linewidth=2, label=f"Cluster {index}")
        ax.fill(angles, values, color=colors[i], alpha=0.25)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), features)
    ax.set_title("Cluster Profile Radar Chart", size=16)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
