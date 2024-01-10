# Billboard to Spotify Playlist Generator

This Python script fetches the Billboard Hot 100 chart for a specified date and creates a private Spotify playlist containing the top 100 songs from that date.

## Prerequisites

- Python 3.x
- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests](https://docs.python-requests.org/en/master/)

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/isotronic/billboard-to-spotify.git
   ```

2. Navigate to the project directory:
   ```bash
   cd billboard-to-spotify
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Obtain Spotify API credentials by creating an application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   
2. Set the following environment variables:
   ```bash
   export SPOTIPY_CLIENT_ID=your_spotify_client_id
   export SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   export SPOTIPY_USER=your_spotify_username
   ```

3. Adjust other parameters in the script as needed, such as the Spotify redirect URI and the scope.

## Usage

1. Run the script:
   ```bash
   python playlist_generator.py
   ```

2. Input the date you want to create a playlist for in the format `YYYY-MM-DD` when prompted.

3. The script will fetch the Billboard Hot 100 chart for the specified date, search for corresponding tracks on Spotify, and create a private playlist with those tracks.

## Notes

- Ensure that your Spotify account has the necessary permissions for playlist modification (`playlist-modify-private` scope).

- The generated playlist will be named based on the chosen date, e.g., "YYYY-MM-DD Billboard Top 100."

## Acknowledgments

- This project uses Spotipy for Spotify API interaction and BeautifulSoup for web scraping.
