import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = "RoyalBalletAndOpera"

if not API_KEY:
    raise EnvironmentError(
        "API_KEY is not set. Add API_KEY=<your_key> to a .env file or set the environment variable before running this script."
    )

def get_playlist_id():

    try:
            
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

       # print(json.dumps(data, indent=4))

        channel_items = data["items"][0]

        channel_playlistID = channel_items["contentDetails"]["relatedPlaylists"]['uploads']

        print(channel_playlistID)

        return channel_playlistID
    
    except requests.exceptions.RequestException as e:
        raise e
    
    
if __name__ == "__main__":
    get_playlist_id()

