"""
Plotting functions for LSTtrends.
Includes radar charts and distribution maps.
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_radar_chart(
    cluster_means,
    features,
    colors,
    output_path=None,
    title="Cluster Profile Radar Chart",
):
    """Generate a radar chart for clustering results."""
    num_vars = len(features)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    for i, (index, row) in enumerate(cluster_means.iterrows()):
        values = row.tolist()
        values += values[:1]
        ax.plot(angles, values, color=colors[i], linewidth=2, label=f"Cluster {index}")
        ax.fill(angles, values, color=colors[i], alpha=0.25)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), features)
    ax.set_title(title, size=16)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300)
    plt.show()
