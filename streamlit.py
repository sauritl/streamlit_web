import streamlit as st
import seaborn as sns
import pandas as pd
from gsheetsdb import connect







st.title("Connect to Google Sheets")
gsheet_url = st.secrets["public_gsheets_url"]
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)


t_array = df_gsheet['Nombre_Completo'].to_numpy()

st.title("Ver el select")

user = st.multiselect("Seleccione Usuario", t_array)


st.title("Data Exploration")


select = st.selectbox("Choose a variable for the x-axis", t_array)

st.write(select)


st.title("Connect to users")
spotify_csv = st.secrets["spotify_csv"]
conn = connect()
rows = conn.execute(f'SELECT * FROM "{spotify_csv}"')
spotify_csv = pd.DataFrame(rows)
to_show = spotify_csv[spotify_csv['user'] == select] 
st.write(to_show)



plost.bar_chart(
    data =to_show,
    bar='artist_genres')

st.write(plost.bar_chart)



