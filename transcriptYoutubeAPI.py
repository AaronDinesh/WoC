from youtube_transcript_api import YouTubeTranscriptApi 

def downloadCaptions(videoID: str):
    # assigning srt variable with the list 
    # of dictionaries obtained by the get_transcript() function
    srt = YouTubeTranscriptApi.get_transcript(videoID)

    # prints the result
    # print(srt)

    # creating or overwriting a file "subtitles.txt" with 
    # the info inside the context manager
    with open(f"captions/{videoID}.txt", "w", encoding="utf-8") as f:
    
            # iterating through each element of list srt
        for i in srt:
            # writing each element of srt on a new line
            f.write("{}\n".format(i))
