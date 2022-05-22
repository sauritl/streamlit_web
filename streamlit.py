import streamlit as st
import pandas as pd
from gsheetsdb import connect


st.write("My First Streamlit Web App")

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)



st.title("Connect to Google Sheets")
gsheet_url = "https://docs.google.com/spreadsheets/d/1y1saTpjqKoFVuNtJYqvrsz-wYnV8P0knjpKv4ZGaIpM/edit?usp=sharing"
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)
