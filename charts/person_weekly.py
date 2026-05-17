from data.preprocessing import preprocess
import matplotlib.pyplot as plt




def individual_weekly_plot(df,name):

    named_df = df[df["name"] == name]

    weekly_counts = (
        named_df.groupby("week")["checkin"]
        .sum()
        .sort_index()
    )

    fig_width = max(8, len(weekly_counts) * 1.2)

    fig, ax = plt.subplots(figsize=(fig_width, 5))

    # Dynamic line plot
    ax.plot(
        weekly_counts.index,
        weekly_counts.values,
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
            ha="center",
            fontsize=10
        )

    # Dynamic x-axis
    ax.set_xticks(weekly_counts.index)

    ax.set_xticklabels(
        [f"Week {i}" for i in weekly_counts.index],
        rotation=45 if len(weekly_counts) > 10 else 0
    )

    # Dynamic y-axis
    ymin = 0
    ymax = weekly_counts.max() + max(2, weekly_counts.max() * 0.1)

    ax.set_ylim(ymin, ymax)

    # Labels
    ax.set_title(
        f"{name} Weekly Checkins",
        fontsize=18
    )

    ax.set_xlabel("Weeks")
    ax.set_ylabel("Total Checkins")

    # Grid
    ax.grid(
        True,
        linestyle="--",
        alpha=0.5
    )

    plt.tight_layout()

    return fig