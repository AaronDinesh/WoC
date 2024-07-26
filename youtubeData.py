from youtube_transcript_api import YouTubeTranscriptApi

import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm

def randomYoutubeID(video_id: str = None):
    
    if video_id == None:
        url = f"https://www.youtube.com/"
    else:
        url = f"https://www.youtube.com/watch?v={video_id}"
    
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    related_ids = []
    
    # Find the script tag containing the related videos data
    scripts = soup.find_all('script')
    for script in scripts:
        if 'var ytInitialData = ' in script.text:
            data = script.text.split('var ytInitialData = ')[1].split(';</script>')[0]

            # Clean the data
            data = data.strip()
            if data.endswith(';'):
                data = data[:-1]
        
            
            try:
                json_data = json.loads(data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                continue
            
            # Extract related video IDs
            try:
                related_videos = json_data['contents']['twoColumnWatchNextResults']['secondaryResults']['secondaryResults']['results']
                for video in related_videos:
                    if 'compactVideoRenderer' in video:
                        video_id = video['compactVideoRenderer']['videoId']
                        related_ids.append(video_id)
                
            except KeyError as e:
                print(f"Error accessing JSON structure: {e}")
                continue

    return related_ids

def downloadCaptions(videoID: str):
    try:
        # Retrieving a list of dictionaries of the transcript
        srt = YouTubeTranscriptApi.get_transcript(videoID)

        # Writing the transcripts to a .txt file
        with open(f"captions/{videoID}.txt", "w", encoding="utf-8") as f:
        
            # iterating through each element of list srt
            for i in tqdm(srt, desc=f"Downloading ID: {videoID}"):
                # writing each element of srt on a new line
                f.write("{}\n".format(i["text"]))
    except:
        print("Error! Skipping videoID " + videoID)
