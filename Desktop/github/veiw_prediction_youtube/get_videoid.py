from tqdm import tqdm
from googleapiclient.discovery import build
import json
import pandas as pd
import codecs
import urllib.request
import numpy as np
DEVELOPER_KEY = "AIzaSyAv2VeF7B48NViNcGfSCUZRiIcy9uyFq6A"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

playlistId = "PLBEss1hdhNp1KlL-TjXskhL1H-QOUMMym"
items = {"videoid":[],"title":[],"view":[],"good":[],"bad":[]}


def _get_playlistid(next_page_token = ""):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    videos_response = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlistId,
        maxResults=50,
        pageToken=next_page_token
    ).execute()
    new = pd.DataFrame()
    for item in tqdm(videos_response.get("items", [])):
        stats = youtube.videos().list(
            part='statistics',
            id=item["contentDetails"]["videoId"],
        ).execute()
        items["title"].append(item['snippet']['title'])
        items["videoid"].append(item['snippet']['resourceId']['videoId'])
        if stats["items"] != []:
            s=stats["items"][0]["statistics"]
            items["view"].append(int(s["viewCount"]) if "viewCount" in s else None)
            items["good"].append(int(s["likeCount"]) if "likeCount" in s else None)
            items["bad"].append(int(s["dislikeCount"]) if "dislikeCount" in s else None)
        else: 
            items["view"].append(None)
            items["good"].append(None)
            items["bad"].append(None)

    if 'nextPageToken' in videos_response:
       _get_playlistid(videos_response["nextPageToken"])

if __name__ == "__main__":
    _get_playlistid()

    data = pd.DataFrame(np.array(list(items.values())).T, columns = list(items.keys()))
    data.to_csv("./data/train.csv",index = None)