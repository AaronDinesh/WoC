import operator
import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.http import MediaIoBaseDownload
import io
import googleapiclient.errors
import google.auth.exceptions
import os
import logging
import json
import time
import atexit
from enum import Enum

class cost(Enum):
    CAPTION_LIST = 50
    CAPTION_DOWNLOAD = 200
    ERROR = 1

class youtubeAPI:
    def __init__(self, scope: list[str] = None, client_secret_file: str = None, log: bool = True) -> None:
        #os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        self.scope: list[str] = ["https://www.googleapis.com/auth/youtube.force-ssl"] if scope == None else scope
        breakpoint()
        self.service_name: str = "youtube"
        self.api_verson: str = "v3"
        self.client_secret_file: str = "client_secret.json" if client_secret_file == None else client_secret_file
        self.flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(self.client_secret_file, self.scope)
        self.credentials = None
        self.client = None
        if log:
            self.logger = logging.getLogger("Logger")
       
        self.quota = 0
        if(os.path.exists("quota.json")):
            mod_time = os.path.getmtime("quota.json")
            # Checks to see if the last modified date is less than the current date.
            # The quota resets at the start of each day.
            if(int(time.strftime("%d",time.gmtime())) < int(time.strftime("%d", mod_time))):
                with open("quota.json", "r") as f:
                    self.quota = json.load(f)

    
    def authenticate(self) -> bool:
        self.credentials = self.flow.run_local_server()
        
        if self.credentials == None:
            self.logger.error("Failed to authenticate")
            return False
        
        try:
            self.client = googleapiclient.discovery.build(self.service_name, self.api_verson, credentials=self.credentials) 
        except google.auth.exceptions.MutualTLSChannelError:
            self.logger.error("Mutual TLS Channel Error")

        return True
    
    def updateQuota(self, operation: Enum) -> None:
        '''
            This is a best guess of the total useage. Since I can't find a way to query the total useage directly, this
            will have to do. They are pulled from here https://developers.google.com/youtube/v3/determine_quota_cost 
        '''

        self.quota += operation.value    

    def apiShutdown(self) -> None:
        with open("quota.json", "w", encoding='utf-8') as f:
            json.dumps(str(self.quota), f)
    

    # Might not need this since most videos should have an english transcription? Plus we can avoid the 50 credit useage. 
    def listCaptions(self, part: str = None, videoID: str = None):
        request = self.client.captions().list(part=part, videoId=videoID)
        response = request.execute()
        self.updateQuota(cost.CAPTION_LIST)
        return response
    
    def downloadCaptions(self, videoID: str):
        request = self.client.captions().download(id=videoID, tlang="en")
        with open(f"captions/{videoID}.txt", "w") as file_handle:
            #file_handle = io.FileIO(f"captions/{videoID}.txt")
            download = MediaIoBaseDownload(file_handle, request)
            complete = False
            while not complete:
                status, complete = download.next_chunk()
                breakpoint()
            self.updateQuota("CAPTION_DOWNLOAD")

