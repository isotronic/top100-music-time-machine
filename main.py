import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIFY_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIFY_USER = os.environ["SPOTIFY_USER"]
SPOTIFY_REDIRECT_URI = "https://example.com"
SCOPE = "playlist-modify-private"

# ask user which date they want to create a playlist for and fetch the corresponding page on billboard.com
chosen_date = input("Which date do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"{BILLBOARD_URL}{chosen_date}")
web_page = response.text

# go through the website, pick out the song titles and artist names and combine them into a dictionary
soup = BeautifulSoup(web_page, "html.parser")
title_tags = soup.select(selector="li h3", class_="c-title")
song_titles = [title.get_text().strip() for title in title_tags][:100]
artist_names = [name.next_element.next_element.next_element.text.strip() for name in title_tags][:100]
song_and_artist = dict(zip(song_titles, artist_names))
print(f"Top 100 Billboard songs for {chosen_date}, were added to the list.")

# authenticate the user on spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope=SCOPE,
                                               cache_path="token.txt",
                                               username=SPOTIFY_USER,))
user_id = sp.current_user()["id"]

# find all the spotify song uri's from the previously created dictionary and add them to a list.
# if they don't exist, then skip them
print("Searching for songs on Spotify...")
track_uris = []
for (song, artist) in song_and_artist.items():
    try:
        result = sp.search(f"track: {song} artist: {artist}", type="track")
        uri = result["tracks"]["items"][0]["uri"]
        track_uris.append(uri)
    except IndexError:
        print("Song not found on Spotify. Skipped.")
print(f"Found {len(track_uris)} songs on Spotify.")

# create a playlist for the current user on spotify and add each track that was found to that playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{chosen_date} Billboard Top 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=track_uris)
print("Playlist was successfully created and the songs added to it.")

