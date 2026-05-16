import seaborn as sns
from data_cleaning import load_and_clean_data
from preprocessing import preprocess
import matplotlib.pyplot as plt

df = preprocess()

import matplotlib.pyplot as plt
import numpy as np

def weekly_plot():

    weekly_counts = (
        df.groupby("week")["checkin"]
        .sum()
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot
    ax.plot(
        weekly_counts.index,
        weekly_counts.values, #type: ignore
        marker="o",
        linewidth=2
    )

    # Value labels
    for x, y in zip(weekly_counts.index, weekly_counts.values):
        ax.annotate(
            f"{y}",
            (x, y),
            textcoords="offset points",
            xytext=(0, 8),
            ha="center"
        )

    # Dynamic x-axis
    ax.set_xticks(weekly_counts.index)
    ax.set_xticklabels(
        [f"Week {i}" for i in weekly_counts.index],
        rotation=0
    )

    # Dynamic y-axis
    ymin = max(0, weekly_counts.min() - 5)
    ymax = weekly_counts.max() + 5

    ax.set_ylim(ymin, ymax)

    # Better spacing
    ax.margins(x=0.05)

    # Labels
    ax.set_title("Weekly Checkin", fontsize=16)
    ax.set_xlabel("Weeks")
    ax.set_ylabel("Total Checkins")

    # Grid
    ax.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()

    return fig