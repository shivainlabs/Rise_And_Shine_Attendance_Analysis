import seaborn as sns
from data_cleaning import load_and_clean_data
from preprocessing import preprocess
import matplotlib.pyplot as plt

df = preprocess()

def weekly_plot():
    fig, ax = plt.subplots(figsize=(8, 4))
    weekly_counts = df.groupby("week")["checkin"].sum()
    ax.plot(weekly_counts.index,weekly_counts.values) #type: ignore
    ax.set_title("Weekly Checkin")
    return fig