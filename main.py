import config
import gpt
import playlists

SPOTIFY_USERNAME = config.username


def search():
    print("Here you can search by a number of things")
    track_name = input('Please input track name followed by artist: ')
    search_results = config.sp.search(q=track_name, limit=1)
    track_id = search_results['tracks']['items'][0]['id']
    return track_id


def display_menu():
    print("Welcome to your personal spotify engine! Please Select a task:")
    print("1. Search")
    print("2. Create Playlist")
    print("3. Talk to God")


while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print(search())
    elif choice == "2":
        playlists.playlist_based()
    elif choice == "3":
        gpt.main()
