import requests
import json

import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")

api_key=os.getenv("api_key")
handle='MrBeast'
print(api_key)

def channel_playlist():
    try:
        url=f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={handle}&key={api_key}"

        response=requests.get(url)
        #print(response)
        response.raise_for_status()
        data=response.json()

        #print(json.dumps(data,indent=4))

        channel=data["items"][0]
        playlistdata=channel["contentDetails"]["relatedPlaylists"]['uploads']
        print(playlistdata)
    except requests.exceptions.RequestException as e:
        raise e
    
if __name__=="__main__":
    channel_playlist()