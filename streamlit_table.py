import pandas as pd
import streamlit as st

df = pd.read_excel("C:\\Users\\RSPRASAD\\OneDrive - Danaher\\Learning\\LS_Crawler\\" \
    "combined_life_sciences_articles_17th_Nov.xlsx")
st.write(df)