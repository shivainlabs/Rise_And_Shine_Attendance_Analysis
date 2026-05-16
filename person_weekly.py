from preprocessing import preprocess
import matplotlib.pyplot as plt


df = preprocess()

def individual_weekly_plot(name):

    # Filter person
    named_df = df[df["name"] == name]

    # Weekly aggregation
    weekly_counts = (
        named_df.groupby("week")["checkin"]
        .sum()
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    # Dynamic bar plot
    bars = ax.bar(
        weekly_counts.index.astype(str),
        weekly_counts.values
    )

    # Value labels on bars
    for bar in bars:
        height = bar.get_height()

        ax.annotate(
            f"{int(height)}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 5),
            textcoords="offset points",
            ha="center"
        )

    # Dynamic labels
    ax.set_xticks(range(len(weekly_counts.index)))
    ax.set_xticklabels(
        [f"Week {i}" for i in weekly_counts.index]
    )

    # Dynamic y-axis scaling
    ymax = max(weekly_counts.values.max() + 2, 5)
    ax.set_ylim(0, ymax)

    # Titles
    ax.set_title(f"{name} Weekly Checkins", fontsize=16)
    ax.set_xlabel("Weeks")
    ax.set_ylabel("Total Checkins")

    # Grid
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()

    return fig