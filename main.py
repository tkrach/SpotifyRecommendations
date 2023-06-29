import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.client_id,
                                               client_secret= config.client_secret,
                                               redirect_uri="http://localhost:8000",
                                               scope="user-library-read"))
SPOTIFY_USERNAME = config.username
results = sp.current_user_saved_tracks()

for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
