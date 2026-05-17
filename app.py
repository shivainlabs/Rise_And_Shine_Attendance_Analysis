import pandas as pd
import streamlit as st
from data.preprocessing import preprocess
from charts.person_weekly import individual_weekly_plot
from components.dashboard import main_dashboard


st.set_page_config(layout="wide",page_title="Rise and Shine")


# Load Data

df = preprocess()

# Sidebar
page = st.sidebar.radio(
    "Navigation",
    [
        "📊 Dashboard",
        "👤 Individual Analysis",
        "🚫 Inactive Users",
        "🗂 Raw Data"
    ]
)


# Dashboard

if page == "📊 Dashboard":
    main_dashboard(df)    



# Individual Analysis
elif page == "👤 Individual Analysis":
    st.title("👤 Individual Weekly Analysis")
    name = st.selectbox("Total Weekly Detail",list(df["name"].unique()))
    name_btn = st.button("Show...")
    if name_btn:
        fig = individual_weekly_plot(df,name)
        st.pyplot(fig)
 
 
elif page == "🚫 Inactive Users":
    st.title("🚫 Inactive Users")
    st.write("Will update soon....")
    

else:
    st.title("🗂 Raw Data")
    st.dataframe(df.tail(100))

