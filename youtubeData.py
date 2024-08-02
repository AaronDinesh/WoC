from youtube_transcript_api import YouTubeTranscriptApi

import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm
import numpy as np
import os

def __randomYoutubeIDs(video_id: str = None):

    if video_id == None:
        url = "https://www.youtube.com/feed/trending"
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
            pattern = r"(?<='videoId': ').*?(?=')"
            matches = re.findall(pattern, str(json_data))
            matches = list(set(matches))
            for match in matches:
                if (match != video_id and not os.path.exists(f"captions/{match}.txt")):
                # if (match != video_id):
                    related_ids.append(match)

            # print("\nRELATED IDS:")
            # print(related_ids)
            # print("\n")


            # # Extract related video IDs
            # try:
            #     if video_id == None:
            #         tabs = json_data['contents']['twoColumnBrowseResultsRenderer']['tabs']

            #         for tab in tabs:
            #             if len(related_ids) >= 10:
            #                 break


            #             tab_contents = tab['tabRenderer']['content']['sectionListRenderer']['contents']
            #             for tab_content in tab_contents:
            #                 items = tab_content['itemSectionRenderer']['contents']

            #                 for item in items:
            #                     videos = item['shelfRenderer']['content']['expandedShelfContentsRenderer']['items']

            #                     for video in videos:
            #                         videoID = video['videoRenderer']['videoId']
            #                         related_ids.append(videoID)
            #     else:
            #         related_videos = json_data['contents']['twoColumnWatchNextResults']['secondaryResults']['secondaryResults']['results']
            #         for i in range(min(10, len(related_videos))):
            #             if 'compactVideoRenderer' in related_videos[i]:
            #                 videoID = related_videos[i]['compactVideoRenderer']['videoId']
            #                 related_ids.append(videoID)

            # except KeyError as e:
            #     print(f"Error accessing JSON structure: {e}")
            #     continue 
    
    # if (len(related_ids) == 0):
    #     print("\nDATA DUMP:")
    #     print(video_id)
    #     print("\n")
    #     print(json_data)

    #     # Writing the transcripts to a .txt file
    #     with open(f"jsonData.txt", "w", encoding="utf-8") as f:
    #         f.write(str(json_data))

    return np.random.choice(related_ids, min(5, len(related_ids)), replace=False)

def generateRandomYoutubeIDs(video_id: str):
    related_ids = __randomYoutubeIDs(video_id)
    np.concatenate((related_ids, __randomYoutubeIDs()), axis=0)

    return str(np.random.choice(related_ids, 1 ,replace=False)[0])

def downloadCaptions(videoID: str):
    try:
        # Retrieving a list of dictionaries of the transcript
        srt = YouTubeTranscriptApi.get_transcript(videoID, languages=['en', 'en-US', 'en-AU', 'en-BZ', 'en-CA', 
                                                                      'en-IE', 'en-JM', 'en-NZ', 'en-ZA', 'en-tt', 
                                                                      'en-GB'])

        # Writing the transcripts to a .txt file
        with open(f"captions/{videoID}.txt", "w", encoding="utf-8") as f:

            # iterating through each element of list srt
            for i in srt:
                # writing each element of srt on a new line
                f.write("{}\n".format(i["text"]))
    except Exception as e:
        print(f"Error: {e}. Skipping videoID " + videoID)
