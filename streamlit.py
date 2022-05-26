import streamlit as st
import pandas as pd
from gsheetsdb import connect
#import functions







st.title("Connect to Google Sheets")
#gsheet_url = st.secrets["public_gsheets_url"]
gsheet_url = "https://docs.google.com/spreadsheets/d/1HgnR9sCktveRSOHqLEm3UdCxSyf5iu5NE72XVZMq2AE/edit?usp=sharing"
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

       
