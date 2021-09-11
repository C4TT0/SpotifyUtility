# Imports

import os
import sys
import colorama
import json
import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from youtube_search import YoutubeSearch
from pytube import YouTube

colorama.init()

# Banner 

banner = '''
===================================
[+] Spotify Playlist Downloader [+]
===================================

[0] Help [ Shows this banner ]
[1] Download Playlist [ Using Playlist Id ]
[99] Exit

To know about how to get Playlist Id visit: https://github.com/Typh0n12/SpotifyPlaylistDownloader

NOTE: You can only download playlists using this, attempting to download albums, individual songs etc will result in an error. This script uses youtube to search and download songs, results may vary.

Made by Typh0n12
Github : https://www.github.com/Typh0n12
'''

# Oauth

auth_manager = SpotifyClientCredentials(client_id='9968e7b74a724a03bced06a465c14663', client_secret='0a07f456aa2347fcbc42476be70e4aac')
sp = spotipy.Spotify(auth_manager=auth_manager)

# Main class

class Main:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id

    def get_track_ids(self):
        music_id_list = []
        playlist = sp.playlist(self.playlist_id)
        for item in playlist['tracks']['items']:
            music_track = item['track']
            music_id_list.append(music_track['id'])
        return music_id_list

    def get_track_name(self, track_ids):
        name_list = []
        for i in range(0, len(track_ids)):
            meta = sp.track(track_ids[i])
            name_list.append(meta['name'])

        return name_list

    def work(self):
        song_data = []
        song_url = []
        watch_url = []
        dest = './Audio'

        name_list = self.get_track_name(self.get_track_ids())
        for i in range(0, len(name_list)):
            results = YoutubeSearch(name_list[i], max_results=1).to_json()
            song_data.append(results)

        for i in range(0, len(song_data)):
            watch_url.append(song_data[i].split(":")[13].split("}")[0].replace("\"", "").replace(" ", ""))
        
        for i in range(0, len(watch_url)):
            url = 'https://www.youtube.com{}'.format(watch_url[i])
            song_url.append(url)

        for i in range(0, len(song_url)):
            yt = YouTube(song_url[i])
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download(output_path=dest)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(yt.title + " has been downloaded successfully")

# Start class

class Start:
    def __init__(self):
        pass
    def start(self):
        print(banner)
        while True:
            choice = input(">>>")
            if choice == "0":
                print(banner)
                continue
            elif choice == "99":
                print("Exitting....")
                sys.exit(0)
            elif choice == "1":
                link = input('[+] Enter Playlist Id: ')
                if len(link) == 22:
                    Main(link).work()
                else:
                    print(colorama.Fore.LIGHTRED_EX + 'Invalid Id' + colorama.Style.RESET_ALL)
            else:
                print(colorama.Fore.LIGHTRED_EX + "Invalid Input" + colorama.Style.RESET_ALL)
                continue

if __name__ == '__main__':
    App = Start()
    App.start()
