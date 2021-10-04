# SpotifyPlaylistDownloader
Tired of listening spotify ads? Then this tool is made for you !

What this tools offer: Download your spotify playlist in .mp3 format for free.
<br><br>
NOTE: This tool is only made for downloading playlist, attempting to download individual tracks, albums, etc will return error. This tool uses youtube to download audio, results may vary,

## Setup

1. Clone this repo
```
git clone https://github.com/Typh0n12/SpotifyPlaylistDownloader.git
```
2. Install it by changing the directory to SpotifyPlaylistDownloader
```
cd SpotifyPlaylistDownloader
python3 setup.py install
```
3. Check for folder. If ./Audio dose not exist then create one in ./SpotifyPlaylistDownloader
4. Run the script
``` 
python3 main.py
```

# Getting playlist Id

This script takes playlist id as input and then does further processing so it is important to know how to get your playlist id.

Spotify playlist links exists in two formats

1. https://open.spotify.com/playlist/3v3Vw07VKG1dBh8NjFduQ0

In the link given above, 3v3Vw07VKG1dBh8NjFduQ0 is your playlist id

2. https://open.spotify.com/playlist/3v3Vw07VKG1dBh8NjFduQ0?si=700186a8b4864071

In the link given above, 3v3Vw07VKG1dBh8NjFduQ0 is your playlist id, the unique string between / and ?

To get link in the format 1, simply open your playlist in a web browser and copy the link.
To get link in the format 2, open your spotify playlist, then copy playlist id via the interference.

# Final Notes

If you encounter any bug or issue in this tool then feel free to open a issue.
