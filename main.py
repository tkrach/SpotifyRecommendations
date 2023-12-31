import config
import gpt
import playlists


def search():
    print("Here you can search a song and receive the song ID in response.")
    track_name = input('Please input track name followed by artist: ')
    search_results = config.sp.search(q=track_name, limit=1)
    track_id = search_results['tracks']['items'][0]['id']
    return track_id


def display_menu():
    print("Welcome to your personal spotify engine! Please Select a task:")
    print("1. Search")
    print("2. Create Playlist")


while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print(search())
    elif choice == "2":
        print("1. ChatGPT based playlist generation")
        print("2. Spotify only based playlist generation")
        choice2 = input("Enter your choice: ")
        if choice2 == "1":
            gpt.menu()
        elif choice2 == "2":
            playlists.playlist_based()
        else:
            print("Choice not recognized. Please try again")
    else:
        print("Choice not recognized. Please try again")
