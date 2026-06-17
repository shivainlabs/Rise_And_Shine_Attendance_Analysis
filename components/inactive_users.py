from datetime import datetime
from zoneinfo import ZoneInfo
import streamlit as st
import pandas as pd


def inactive_users(df):

    today_date = pd.to_datetime(datetime.now(ZoneInfo("Asia/Kolkata")).date())
        
    filtered_df = df[df["date"] == today_date]    
    current_week = filtered_df.iloc[0]["week"]   
        
    prev_week = current_week -  1


    week_df = df.query(f"week == {prev_week}")

    inactive_df = (
        week_df.groupby("name")
        .agg(
            weekly_checkins=("checkin","sum"),
            last_checkin=("date","max") # Wrong here
        )
        .reset_index()
    )

    inactive_df = inactive_df[
        inactive_df["weekly_checkins"] < 4
    ].sort_values("weekly_checkins")

    st.metric(
        "Inactive Users (<4 check-ins)",
        len(inactive_df)
    )

    st.dataframe(
        inactive_df,
        use_container_width=True
    )