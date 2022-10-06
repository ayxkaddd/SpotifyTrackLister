import config
from colorama import init, Fore

init(autoreset=True)

suckmymeme = """
                 ⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
                  ⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
                    ⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
                   ⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
               ⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
               ⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
               ⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
               ⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
               ⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
               ⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
               ⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """


print(Fore.CYAN + suckmymeme)

import spotipy
from spotipy.oauth2 import SpotifyOAuth

oauth = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.client_id, client_secret=config.client_secret, scope="user-library-read", redirect_uri=config.redirect_uri))


def get_tracks(offset):
    begin = 0
    tracks = oauth.current_user_saved_tracks(limit=20, offset=offset)
    items = tracks.get("items")
    tracks_file = open(config.file_name, "a", encoding="utf-8")
    for item in items:
        begin += 1
        track = item.get("track")
        track_name = track.get("name")
        artist = track.get("artists")
        artist = artist[0]
        artist_name = artist.get("name")

        tracks_string = f"{artist_name} - {track_name}\n"
        tracks_file.write(tracks_string)
        print(Fore.CYAN + f"[{begin}] {artist_name} - {track_name}")
        end = begin
    config.tracks_count += end
    print(Fore.GREEN + f"\t\t\t\t\t\t\t\t\twrited {end} tracks")
    tracks_file.close()


def main():
    offset = -20
    limit = 20
    count_of_added_tracks = your_number
    for i in range(round(count_of_added_tracks / 20) + 1):
        offset += limit
        get_tracks(offset)
    print(Fore.GREEN + f"\n\t\t\t\t\tDone\n\t\t\t\t\t{config.file_name} filled\n\t\t\t\t\tTotal tracks count - {config.tracks_count}")


if __name__ == "__main__":
    print("///its uglu asf but idc")
    main()
