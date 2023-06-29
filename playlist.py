import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= config.client_id,
                                               client_secret= config.client_secret,
                                               redirect_uri="http://localhost:8000",
                                               scope="playlist-modify-public"))
SPOTIFY_USERNAME = config.username


def create_playlist():
    playlist_name = "My Blank Playlist"
    playlist_description = "This is a blank playlist created using the Spotipy library."

    playlist = sp.user_playlist_create(SPOTIFY_USERNAME, playlist_name, public=True, description=playlist_description)
    return playlist


def main():
    # Create a blank playlist
    playlist = create_playlist()

    # Print the playlist details
    print("Playlist created:")
    print("Name:", playlist['name'])
    print("Owner:", playlist['owner']['display_name'])
    print("Public:", playlist['public'])
    print("Tracks:", playlist['tracks']['total'])


if __name__ == '__main__':
    main()
