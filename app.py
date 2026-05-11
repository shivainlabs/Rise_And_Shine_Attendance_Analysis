import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from data_cleaning import load_and_clean_data
from preprocessing import preprocess
from weekly import weekly_plot


df = preprocess()
# st.dataframe(df)
fig = weekly_plot()

st.title("Rise And Shine")
col1, col2 = st.columns(2)
with col1:
    st.pyplot(fig)

