import pandas as pd
import streamlit as st

df = pd.read_excel("combined_life_sciences_articles_17th_Nov.xlsx")

st.write(df)
