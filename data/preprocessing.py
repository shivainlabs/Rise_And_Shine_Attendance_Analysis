import seaborn as sns
from data.data_cleaning import load_and_clean_data
import pandas as pd
import streamlit as st


start_date = pd.Timestamp("2026-04-27")

@st.cache_data(ttl=30)
def preprocess():
    df = load_and_clean_data()

    df["week"] = ((df["date"] - start_date).dt.days // 7) + 1
    return df