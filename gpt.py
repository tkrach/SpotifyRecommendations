import openai
import config
import recommender
import re

openai.api_key = config.api_key


def menu():
    print("You are now talking to God. Choose your words wisely: ")
    print("1. Create God's Playlist")
    print("2. Create a God Fused Playlist")
    print("3. Give God an Existing Playlist")
    print("4. Talk to God")


def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            gpt_gen_playlist()
        elif choice == "2":
            fusion_playlist()
        elif choice == "3":
            gpt_eats_playlist()
        elif choice == "4":
            query()


def gpt_gen_playlist():
    description = input("Describe the playlist you wish God to create: ")
    num_tracks = input("How many tracks shall God bless you with today? ")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are being used in a program to create song playlists based on a user's description. "
                        "Please only provide song names and no additional text or information "
                        "\nKnowledge cutoff: 2021-09-01\nCurrent date: 2023-03-02"},
            {"role": "assistant", "content": "I understand, I will do my best to provide adequate recommendations"},
            {"role": "user", "content": "Here is the user's description: {} \n Here is the number of tracks you shall "
                                        "provide: {} ".format(description, num_tracks)}
        ]
    )
    assistant_message = completion.choices[0].message['content']
    print("God has blessed you with the following:\n", assistant_message)
    answer = input("Would you like to create a Spotify playlist with these tracks? ")
    if answer == "yes" or "Yes" or "Y" or "y":
        formatted_response = format_response(assistant_message)
        recommender.create_playlist(formatted_response, 0)
    return None


def fusion_playlist():
    # Call gpt_gen_playlist Then get the track IDs with format_response, Pass these track IDs into a new function that
    # functions similarly to playlist_based() ????Maybe create new function with that ability????
    # Call create playlist and add all the tracks to a new playlist
    return None


def format_response(recommendations):
    track_ids = []
    pattern = r'"(.*)" by (.*)'
    matches = re.findall(pattern, recommendations)

    # Format the matches as a list
    track_list = ["{} - {}".format(artist, song) for song, artist in matches]
    print(track_list)
    for track in track_list:
        search_results = config.sp.search(q=track, limit=1)
        track_ids.append(search_results['tracks']['items'][0]['id'])
    print(track_ids)
    return track_ids


def gpt_eats_playlist():
    playlist_id = recommender.playlist_search()

    playlist_tracks = config.sp.playlist_items(playlist_id)

    # Extract the track IDs from the playlist tracks
    track_names = [item['track']['name'] for item in playlist_tracks['items']]
    print(track_names)


def query():
    chat = input("You are now talking to God. Choose your words wisely: ")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as "
                        "possible.\nKnowledge cutoff: 2021-09-01\nCurrent date: 2023-03-02"},
            {"role": "user", "content": "How are you?"},
            {"role": "assistant", "content": "I am doing well"},
            {"role": "user", "content": chat}
        ]
    )
    assistant_message = completion.choices[0].message['content']
    print("God's response:", assistant_message)
