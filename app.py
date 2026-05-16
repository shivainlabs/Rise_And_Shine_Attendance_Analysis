import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from data_cleaning import load_and_clean_data
from preprocessing import preprocess
from weekly_total_checkin import weekly_plot
from person_weekly import individual_weekly_plot
from datetime import datetime
from zoneinfo import ZoneInfo



df = preprocess()
fig = weekly_plot()

st.set_page_config(layout="wide",page_title="Rise and Shine")
st.title("Rise And Shine")
col1, col2 = st.columns(2)
with col1:
    # df["date"] = pd.to_datetime(df["date"]).dt.strftime("%d/%m/%Y")
    today_date = pd.to_datetime(datetime.now(ZoneInfo("Asia/Kolkata")).date())
    
    filtered_df = df[df["date"] == today_date]

    if not filtered_df.empty:
        current_week = filtered_df.iloc[0]["week"]
    else:
        current_week = "No data"
        
    display_date = today_date.strftime("%d/%m/%Y")
    st.text(
        f"Today's Date: {display_date} | Current Week: Week {current_week}")
    st.pyplot(fig)
    


with col2:
    lastest_date = df[df["checkin"]==True].sort_values(by="date",ascending=False).head(1)["date"].values

    lastest_date = lastest_date[0].astype(str).split("T")[0]
    lastest_dt_df = df[df["date"]==lastest_date]
    sent_checkin = lastest_dt_df[lastest_dt_df["checkin"]==True]["name"]
    not_sent = lastest_dt_df[lastest_dt_df["checkin"]==False]["name"]
    st.subheader(f"Lastest Checkins on: {lastest_date}")
    
    st.text("Got checkin from")
    sent_checkin.values
    
    st.text("---")
    not_sent.values


col1, col2 = st.columns(2)
with col1:
    name = st.selectbox("Total Weekly Detail",list(df["name"].unique()))
    name_btn = st.button("Select")
    if name_btn:
        fig = individual_weekly_plot(name)
        st.pyplot(fig)


st.text("For Testing Purpose...")
st.dataframe(df.tail(20))

