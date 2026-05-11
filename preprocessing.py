import seaborn as sns
from data_cleaning import load_and_clean_data
import pandas as pd

df = load_and_clean_data()

start_date = pd.Timestamp("2026-04-27")

def preprocess():
    df["week"] = ((df["date"] - start_date).dt.days // 7) + 1
    return df