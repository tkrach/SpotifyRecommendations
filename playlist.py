import config
import spotipy

SPOTIFY_USERNAME = config.username


def create_playlist():
    playlist_name = "My Blank Playlist"
    playlist_description = "This is a blank playlist created using the Spotipy library."

    playlist = config.sp.user_playlist_create(SPOTIFY_USERNAME, playlist_name, public=True, description=playlist_description)
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
