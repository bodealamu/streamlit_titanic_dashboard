import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title('Titanic Dashboard')

df = pd.read_csv('titani_data.csv')
st.write(df)