import pandas as pd
from gsheetsdb import connect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta
import pandas as pd
#import json
#import requests
#from sklearn import preprocessing
import plotly.graph_objects as go
import plotly.offline as pyo
#from urllib.error import HTTPError
from spotipy import SpotifyException

date = datetime.today() - timedelta(days=30)

gsheet_url_spotify = "https://docs.google.com/spreadsheets/d/1HgnR9sCktveRSOHqLEm3UdCxSyf5iu5NE72XVZMq2AE/edit?usp=sharing"
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url_spotify}"')
spotify_users = pd.DataFrame(rows)

def _extract_current_user_top_tracks(date, limit=100):
       ds = int(date.timestamp()) * 1000
       return sp.current_user_top_tracks(limit=limit, offset = 0, time_range= "medium_term")


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
    return df







