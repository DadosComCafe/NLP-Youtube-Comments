import logging
import pandas as pd
from googleapiclient.discovery import build


def get_video_comments(youtube_credentials: dict) -> pd.DataFrame:
    """

    Args:
        youtube_credentials (dict): A dict with the desired VIDEO_ID and the API_KEY credential

    Returns:
        pd.DataFrame: _description_
    """
    video_id = youtube_credentials.get("VIDEO_ID")
    api_key = youtube_credentials.get("API_KEY")
    logging.info(f"Requesting from {video_id} using the key {api_key}")
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.commentThreads().list(
        part="snippet, replies", videoId=video_id, textFormat="plainText"
    )
    df = pd.DataFrame(columns=["comment", "replies", "date", "username"])
    n = 0
    while request:
        replies = []
        comments = []
        dates = []
        usernames = []

        try:
            response = request.execute()
            for item in response.get("items"):

                comment_textdisplay = (
                    item.get("snippet", {})
                    .get("topLevelComment", {})
                    .get("snippet", {})
                    .get("textDisplay")
                )
                comments.append(comment_textdisplay)

                author_displayname = (
                    item.get("snippet", {})
                    .get("topLevelComment", {})
                    .get("snippet", {})
                    .get("authorDisplayName")
                )
                usernames.append(author_displayname)

                published_date = (
                    item.get("snippet", {})
                    .get("topLevelComment", {})
                    .get("snippet", {})
                    .get("publishedAt")
                )
                dates.append(published_date)

                replycount = item.get("snippet", {}).get("totalReplyCount")

                if replycount > 0:
                    replies.append([])
                    for reply in item.get("replies", {}).get("comments", []):
                        reply = reply.get("snippet", {}).get("textDisplay")
                        replies[-1].append(reply)
                else:
                    replies.append([])

            df2 = pd.DataFrame(
                {
                    "comment": comments,
                    "replies": replies,
                    "user_name": usernames,
                    "date": dates,
                }
            )
            df = pd.concat([df, df2], ignore_index=True)
            #df.to_parquet(f"parquet_files/{video_id}.parquet")
            request = youtube.commentThreads().list_next(request, response)
            n += 1
            logging.info(f"Iterating {n}")
        except Exception as e:
            logging.info(f"An error: {e}")
            break
        return df

if __name__ == "__main__":
    from decouple import config
    logging.basicConfig(level=logging.INFO)
    youtube_credentials = {
        "VIDEO_ID": config("VIDEO_ID"),
        "API_KEY": config("API_KEY")
    }
    comments = get_video_comments(youtube_credentials=youtube_credentials)
    print(comments)