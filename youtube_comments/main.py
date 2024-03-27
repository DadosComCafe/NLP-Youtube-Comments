import logging
import pandas as pd
from googleapiclient.discovery import build
from decouple import config


logging.basicConfig(level=logging.INFO)

def get_video_comments(youtube_credentials: dict) -> pd.DataFrame:
    """_summary_

    Args:
        youtube_credentials (dict): _description_
    """
    video_id = youtube_credentials.get("VIDEO_ID")
    api_key = youtube_credentials.get("API_KEY")
    logging.info(f"Requesting from {video_id} using the key {api_key}")
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.commentThreads().list(
        part="snippet, replies", videoId=video_id, textFormat="plainText"
    )
    df = pd.DataFrame(columns=["comment", "replies", "date", "username"])
    return df