import numpy as np
import pandas as pd

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id='client_id'
client_secret='client_id'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

rock_classics_pl = spotify.user_playlist_tracks('spotify', playlist_id="37i9dQZF1DWXRqgorJj26U", limit=50)
pop_classics_pl = spotify.user_playlist_tracks('sonymusicthelegacy', playlist_id="0O4acIlHb5BnI16ZJFUksE", limit=100)

def create_df(playlist, r):
    durations = np.zeros(r, dtype=int)
    track_name = np.zeros(r, dtype='U50')
    artist_name = np.zeros(r, dtype='U50')
    for count, item in enumerate(playlist['items']):
        track_name[count] = item['track']['name']
        artist_name[count] = item['track']['artists'][0]['name']
        durations[count] = item['track']['duration_ms']
    durations = durations // 1000
    d = {'track_name': track_name, 'artist_name': artist_name, 'durations': durations}
    df = pd.DataFrame(data=d)
    return df


rock_df = create_df(rock_classics_pl, 50)
rock_df

pop_df = create_df(pop_classics_pl, 50)
pop_df

rock_df['durations'].describe()
pop_df['durations'].describe()

rock_df['durations'].hist()
pop_df['durations'].hist()

import matplotlib.pyplot as plt

plt.hist(rock_df['durations'], label='rock', normed=True)
plt.hist(pop_df['durations'], label='pop', normed=True)
plt.legend(loc='upper right')
plt.show()

import seaborn as sns
sns.distplot(rock_df['durations'])
sns.distplot(pop_df['durations'])

sns.distplot(pop_df['durations'], label='pop')
sns.distplot(rock_df['durations'], label='rock')
plt.legend()
plt.show()

