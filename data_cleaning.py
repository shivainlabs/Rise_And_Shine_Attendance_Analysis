import pandas as pd
import numpy as np
import time

# url = "https://docs.google.com/spreadsheets/d/1ZyTt2VrhFFk8ro_E8juDT1KNSMQpgkXWJAxwPNj0Sr4/export?format=csv&gid=0"
# url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQVpCawkt66Cfv04xQmI1QZ_c8paOKSupUxAP_Uf-K7fee-UBQeE9GKiU_7XURlPU6J0fHoMd9Wsw5w/pub?output=csv"
url = f"https://docs.google.com/spreadsheets/d/e/2PACX-1vQVpCawkt66Cfv04xQmI1QZ_c8paOKSupUxAP_Uf-K7fee-UBQeE9GKiU_7XURlPU6J0fHoMd9Wsw5w/pub?output=csv&t={time.time()}"

def load_and_clean_data():
    df = pd.read_csv(url)
    
    df = df.drop(["count week1", "count week2"], axis=1)
    df = df.iloc[0:19]
    df = df.loc[:, ~df.columns.str.contains(r"^count")]

    
    # From wide to Long 
    long_df = df.melt(id_vars=["NAME"],var_name="date",value_name="checkin").rename(columns={"NAME":"name"})
    long_df["checkin"] = (
    long_df["checkin"].astype(str).str.upper().map({
        "TRUE": True,
        "FALSE": False
    })
    )
    
    long_df["date"] = pd.to_datetime(long_df["date"],format="%d/%m/%Y")   
      


    return long_df