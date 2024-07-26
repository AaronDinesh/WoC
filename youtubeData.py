from youtube_transcript_api import YouTubeTranscriptApi 

def downloadCaptions(videoID: str):
    # Retrieving a list of dictionaries of the transcripts
    srt = YouTubeTranscriptApi.get_transcript(videoID)

    # Writing the transcripts to a .txt file
    with open(f"captions/{videoID}.txt", "w", encoding="utf-8") as f:
    
            # iterating through each element of list srt
        for i in srt:
            # writing each element of srt on a new line
            f.write("{}\n".format(i))
