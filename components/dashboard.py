from components.latest_checkins import show_latest_checkins
import streamlit as st
import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo
from charts.weekly_total_checkin import weekly_plot



def main_dashboard(df):
    st.title("📊 Rise And Shine Dashboard")
    today_date = pd.to_datetime(datetime.now(ZoneInfo("Asia/Kolkata")).date())
    
    filtered_df = df[df["date"] == today_date]

    if not filtered_df.empty:
        current_week = filtered_df.iloc[0]["week"]
    else:
        current_week = "No data"
        
    display_date = today_date.strftime("%d/%m/%Y")
    
    metric1,metric2 = st.columns(2)
    metric1.metric(
        "Today's Date",
        display_date
    )

    metric2.metric(
        "Current Week",
        f"Week {current_week}"
    )
    col1,col2 = st.columns(2)
    with col1:
        fig = weekly_plot(df)
        st.pyplot(fig)
    with col2:
        show_latest_checkins(df)
