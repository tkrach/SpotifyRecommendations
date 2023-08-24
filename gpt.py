import openai
import config
import playlists
import re

openai.api_key = config.api_key


def menu():
    print("You are now talking to God. Choose your words wisely: ")
    print("1. Create God's Playlist")
    print("2. Give God an Existing Playlist")
    print("3. Talk to God")


def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            gpt_gen_playlist()
        elif choice == "2":
            gpt_eats_playlist()
        elif choice == "3":
            query()


def gpt_gen_playlist():
    description = input("Describe the playlist you wish God to create: ")
    num_tracks = input("How many tracks shall God bless you with today? ")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are being used in a program to create song playlists based on a user's description. "
                        "Please only provide song and artist names surrounded by double quotes. Like this \"Accordion "
                        "- MF DOOM\" "
                        "\nKnowledge cutoff: 2021-09-01\nCurrent date: 2023-03-02"},
            {"role": "assistant", "content": "I understand, I will do my best to provide adequate recommendations"},
            {"role": "user", "content": "Here is the user's description: {} \n Here is the number of tracks you shall "
                                        "provide: {} ".format(description, num_tracks)}
        ]
    )
    assistant_message = completion.choices[0].message['content']
    print("God has blessed you with the following:\n", assistant_message)
    formatted_response = format_response(assistant_message)

    answer = input("Would you like to create a Spotify playlist with these tracks? ")
    if answer == "yes" or "Yes" or "Y" or "y":
        name, owner = playlists.create_playlist(formatted_response, 0)

        q1 = input("Would you like to use spotify's algorithms to enhance this playlist?")
        if q1 == "yes" or "Yes" or "y" or "Y":
            playlists.playlist_based(name, owner)
    return None


def gpt_eats_playlist():
    playlist_id = playlists.playlist_search()

    playlist_tracks = config.sp.playlist_items(playlist_id)
    num_tracks = input("How many tracks would you like to enhance your playlist with? ")
    # Extract the track IDs from the playlist tracks
    track_names = [item['track']['name'] for item in playlist_tracks['items']]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are being used in a program to add songs to existing playlists based on supplied input "
                        "of a list of songs."
                        "Please only provide song and artist names surrounded by double quotes. Like this \"Accordion "
                        "- MF DOOM\" "
                        "\nKnowledge cutoff: 2021-09-01\nCurrent date: 2023-03-02"},
            {"role": "assistant", "content": "I understand, I will do my best to provide adequate recommendations"},
            {"role": "user", "content": "Here is the list of song's in the playlist: {} \n Here is the number of "
                                        "tracks you shall "
                                        "provide: {} ".format(track_names, num_tracks)}
        ]
    )
    assistant_message = completion.choices[0].message['content']
    print("God's response:", assistant_message)
    formatted = format_response(assistant_message)
    playlists.add_tracks(formatted, playlist_id)


def format_response(recommendations):
    track_ids = []
    pattern = r'"(.*)"'
    matches = re.findall(pattern, recommendations)
    print(matches)
    # Format the matches as a list
    # pattern = r'\d+\.\s(.+?)(?:\n|$)'
    # matches = re.findall(pattern, recommendations)
    track_list = []
    track_list = matches
    # for song, artist in matches:
    # if artist:
    #   track_list.append(f"{song} - {artist}")
    # else:
    #   track_list.append(song)
    print(track_list)
    for track in track_list:
        search_results = config.sp.search(q=track, limit=1)
        print(search_results)
        track_ids.append(search_results['tracks']['items'][0]['id'])
    print(track_ids)
    return track_ids


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
