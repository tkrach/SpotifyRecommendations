import config
import math


def playlist_based(playlist_id, owner):
    if playlist_id is None:
        playlist_id = playlist_search()
    # Retrieve the playlist tracks
    playlist_tracks = config.sp.playlist_items(playlist_id)

    # Extract the track IDs from the playlist tracks
    track_ids = [item['track']['id'] for item in playlist_tracks['items']]

    # Calculate the number of iterations required based on the playlist size
    num_iterations = math.ceil(len(track_ids) / 5)

    # Initialize an empty list to store the recommendations
    all_recommendations = []
    # Iterate through the playlist tracks in groups of 5
    for i in range(num_iterations):
        # Calculate the start and end indices for the current group
        start_idx = i * 5
        end_idx = start_idx + 5

        # Get the current group of track IDs
        seed_tracks = track_ids[start_idx:end_idx]

        # Make the recommendation request for the current group of seed tracks
        recommendations = config.sp.recommendations(seed_tracks=seed_tracks, limit=10)

        # Append the recommendations to the overall list
        all_recommendations.extend(recommendations['tracks'])

    # Print the combined recommendations
    for idx, track in enumerate(all_recommendations):
        print(idx, track['name'])
    if owner is None:
        create_playlist(all_recommendations, 1)
    else:
        track_ids = [track['id'] for track in all_recommendations]
        add_tracks(track_ids, playlist_id)
    return None


def playlist_search():
    playlist_id = None
    # Define the playlist name and owner name
    target_playlist_name = input("Please enter playlist name: ")
    target_owner_name = input("Please enter playlist owner name: ")
    # Retrieve playlists
    playlists = config.sp.user_playlists(target_owner_name)
    # Iterate over the playlists and find the matching playlist
    for playlist in playlists['items']:
        if playlist['name'] == target_playlist_name:
            playlist_id = playlist['id']
            print("Playlist ID:", playlist_id)
            break

    if 'playlist_id' == None:
        print("Playlist not found.")
    return playlist_id


def add_tracks(tracks, playlist_id):
    config.sp.playlist_add_items(playlist_id=playlist_id, items=tracks)
    return None


def create_playlist(recommendations, calling_function):
    playlist_name = input("Please enter playlist name: ")
    playlist_description = input("Please enter playlist description: ")
    config.scope = "playlist-modify-private"
    playlist = config.sp.user_playlist_create(config.username, playlist_name, public=True,
                                              description=playlist_description)
    playlist_id = playlist['id']
    if calling_function == 1:
        track_ids = [track['id'] for track in recommendations]
        config.sp.playlist_add_items(playlist_id, track_ids)
    else:
        config.sp.playlist_add_items(playlist_id, recommendations)

    print("Playlist created:")
    print("Name:", playlist['name'])
    print("Owner:", playlist['owner']['display_name'])
    print("Public:", playlist['public'])
    print("Tracks:", playlist['tracks']['total'])
    return playlist_id, playlist['owner']