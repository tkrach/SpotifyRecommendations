import config
import math


def get_recommendations():
    results = config.sp.current_user_saved_tracks(limit=5)
    track_ids = [item['track']['id'] for item in results['items']]  # Extract track IDs

    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

    recommends = config.sp.recommendations(seed_tracks=track_ids, limit=10)  # Pass track IDs as seed_tracks
    # Print recommendations with only track name
    for idx, track in enumerate(recommends['tracks']):
        print(idx, track['name'])
    # Print recommendations with only track ID
    for idx, track in enumerate(recommends['tracks']):
        print(idx, track['id'])


def playlist_based(playlist):
    # Define the playlist ID
    playlist_id = playlist

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
