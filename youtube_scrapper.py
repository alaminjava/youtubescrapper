YOUR_YOUTUBE_API_KEY = "AIzaSyBscSkiLIPejmZ7b-L33rlCw6WAG2ODxvE"


YOUR_YOUTUBE_CHANNEL_ID = input("Enter your value: ")


import pandas as pd
from googleapiclient.discovery import build

# Set up the YouTube Data API client
api_key = YOUR_YOUTUBE_API_KEY  # Replace with your YouTube API key
youtube = build("youtube", "v3", developerKey=api_key)

def get_youtube_channel_videos(channel_id):
    videos = []
    next_page_token = None

    while True:
        # Fetch the videos from the channel
        response = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for item in response["items"]:
            if "videoId" in item["id"]:
                video_id = item["id"]["videoId"]
                video_title = item["snippet"]["title"]
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                videos.append({"Title": video_title, "URL": video_url})

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return videos

def main():
    channel_id = YOUR_YOUTUBE_CHANNEL_ID  # Replace with the ID of the YouTube channel you want to scrape
    videos = get_youtube_channel_videos(channel_id)

    df = pd.DataFrame(videos)
    df.to_excel("youtube_videos.xlsx", index=False)

    print("Videos saved to youtube_videos.xlsx")

if __name__ == "__main__":
    main()

