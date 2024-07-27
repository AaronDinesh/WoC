from pydoc import cli
import networkx as nx
from youtubeAPI import youtubeAPI
import woc_utils as wu
import youtubeData as ytd
import fnmatch
import os
import numpy as np

def main():
    # wu.chunker("test.txt")

    # client = youtubeAPI(client_secret_file="client_secret.json")
    # ret = client.authenticate()
    # client.downloadCaptions("eVli-tstM5E")
    # client.apiShutdown() 
    
    next_id = "A5w-dEgIU1M"
    
    while len(fnmatch.filter(os.listdir('captions/'), '*.txt')) < 100:
        if(not os.path.exists(f"captions/{next_id}.txt")):
            ytd.downloadCaptions(next_id)
        else:
            print(f"ID: {next_id} exists. Skipping...")

        relatedIDs = ytd.randomYoutubeID(next_id)
        np.concatenate((relatedIDs, ytd.randomYoutubeID()), axis=0)
        
        next_id = str(np.random.choice(relatedIDs, 1 ,replace=False)[0])


if __name__ == "__main__":
    main()
