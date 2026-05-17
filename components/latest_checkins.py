import streamlit as st

def show_latest_checkins(df):
    latest_date = df[df["checkin"]==True]["date"].max()

    # latest_date = (
    #     df[df["checkin"] == True]
    #     .sort_values(by="date", ascending=False)
    #     .head(1)["date"]
    #     .values
    # )


    latest_dt_df = df[df["date"] == latest_date]

    checked_in = (
        latest_dt_df[latest_dt_df["checkin"] == True]["name"].sort_values().tolist()
    )

    missed = (
        latest_dt_df[latest_dt_df["checkin"] == False]["name"].sort_values().tolist()
    )

    st.subheader(
        f"📅 Latest Checkins — {latest_date.strftime('%d/%m/%Y')}"
    )

    col1, col2 = st.columns(2)
    
    # checked in
    with col1:
        st.success(
            f"✅ Submitted ({len(checked_in)})"
        )
        for person in checked_in:
            st.markdown(f"- {person}")
            
     # Missed
    with col2:

        st.error(
            f"❌ Missed ({len(missed)})"
        )

        for person in missed:
            st.markdown(f"- {person}")
    