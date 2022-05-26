import pandas as pd
from gsheetsdb import connect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta
import pandas as pd
#import json
#import requests
#from sklearn import preprocessing
#import plotly.graph_objects as go
#import plotly.offline as pyo

from spotipy import SpotifyException

date = datetime.today() - timedelta(days=30)

gsheet_url_spotify = "https://docs.google.com/spreadsheets/d/1HgnR9sCktveRSOHqLEm3UdCxSyf5iu5NE72XVZMq2AE/edit?usp=sharing"
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url_spotify}"')
spotify_users = pd.DataFrame(rows)

def _extract_current_user_top_tracks(date, limit=100):
       ds = int(date.timestamp()) * 1000
       return sp.current_user_top_tracks(limit=limit, offset = 0, time_range= "medium_term")

global df

def get_df(df_users):    
    artist_name = []
    track_name = []
    track_popularity = []
    artist_id = []
    track_id = []
    area_df = []
    name_df = []
    n= -1
    global df
    global sp
    for index, row in df_users.iterrows():
        n += 1
        area = row["Area"]
        name = row["Nombre_Completo"]
        #print(name)
        sp = spotipy.Spotify(row['Token_Spotify'])
        #print(area)
        #print(name)
        for i in range(0,50,50):
                    try:
                        _extract_current_user_top_tracks(date)["items"]
                        #print(n)
                        #print(name)
                        #print(area)
                    except  SpotifyException as err:
                        continue
                        #if err.code == 401:
                            #print(err.code)
                            #print(n)
                            #area.drop(n)
                            #print(n)
                            #print(area)
                    else:
                        track_results = _extract_current_user_top_tracks(date)["items"]
                        for i,r in enumerate(track_results):
                                        artist_name.append(r["artists"][0]["name"]),
                                        artist_id.append(r["artists"][0]["id"]),
                                        track_name.append(r["name"]),
                                        track_id.append(r["id"]),
                                        track_popularity.append(r["popularity"])
                                        #print(name)
                                        name_df.append(name)
                                        area_df.append(area)
                                        #print(name_df)

                                        df = pd.DataFrame({'artist_name' : artist_name, 'artist_id' : artist_id, 'track_name' : track_name, 'track_id' : track_id, 'track_popularity' : track_popularity})
                                        df['user']= name_df
                                        df['area']=area_df
    df.to_csv('users_vc.csv')
    return df
    


get_df(spotify_users)

df_current_user_top_tracks = pd.read_csv('users_vc.csv')

#print(df.head())

artist_popularity = []
artist_genres = []
artist_followers = []
for a_id in df_current_user_top_tracks.artist_id:
  artist = sp.artist(a_id)
  artist_popularity.append(artist['popularity'])
  artist_genres.append(artist['genres'][0])
  artist_followers.append(artist['followers']['total'])

df_current_user_top_tracks =df_current_user_top_tracks.assign(artist_popularity=artist_popularity, artist_genres=artist_genres, artist_followers=artist_followers)
#df_current_user_top_tracks.head()




track_features = []
danceability = []
for t_id in df_current_user_top_tracks['track_id']:
    af = sp.audio_features(t_id)
    track_features.append(af)
tf_df = pd.DataFrame(columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'])
for item in track_features:
  for feat in item:
    tf_df = tf_df.append(feat, ignore_index=True)
#print(tf_df.head())

new = pd.concat([tf_df,df_current_user_top_tracks], axis=1, join="inner")

#print(new.info())








st.title("Connect to Google Sheets")
gsheet_url = st.secrets["public_gsheets_url"]
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)





t_array = df_gsheet['Nombre_Completo'].to_numpy()

st.title("Ver el select")

#user = st.multiselect("Seleccione Usuario", t_array)

st.title("Data Exploration")


user = st.selectbox("Choose a variable for the x-axis", t_array)

st.write(select)

st.write(df_filtered= new['user'] == user)

       
