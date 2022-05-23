import streamlit as st
import pandas as pd
from gsheetsdb import connect


st.write("My First Streamlit Web App")

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)



st.title("Connect to Google Sheets")
gsheet_url = st.secrets["public_gsheets_url"]
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)


st.title("Select the user")
gsheet_url_spotify = "https://docs.google.com/spreadsheets/d/1HgnR9sCktveRSOHqLEm3UdCxSyf5iu5NE72XVZMq2AE/edit?usp=sharing"
conn = connect()
rows = conn.execute(f'SELECT user FROM "{gsheet_url}"')
spotify_users = pd.DataFrame(rows)
st.write(df_gsheet)
