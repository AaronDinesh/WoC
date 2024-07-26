from youtube_transcript_api import YouTubeTranscriptApi

import undetected_chromedriver as uc

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Add uBlock Origin to the Chrome Driver
chop = webdriver.ChromeOptions()
chop.add_extension('CJPALHDLNBPAFIAMEJDNHCPHJBKEIAGM_1_57_0_0.crx')
chop.add_argument('--headless=new')
chop.add_argument('--start-maximized')
driver = webdriver.Chrome(options = chop)

def randomYoutubeID(i: int):
    driver.get('youtube.com')

def downloadCaptions(videoID: str):
    # Retrieving a list of dictionaries of the transcripts
    srt = YouTubeTranscriptApi.get_transcript(videoID)

    # Writing the transcripts to a .txt file
    with open(f"captions/{videoID}.txt", "w", encoding="utf-8") as f:
    
            # iterating through each element of list srt
        for i in srt:
            # writing each element of srt on a new line
            f.write("{}\n".format(i))
