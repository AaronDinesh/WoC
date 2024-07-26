from pydoc import cli
import networkx as nx
from youtubeAPI import youtubeAPI
import woc_utils as wu
import youtubeData as ytd

def main():
    # wu.chunker("test.txt")

    # client = youtubeAPI(client_secret_file="client_secret.json")
    # ret = client.authenticate()
    # client.downloadCaptions("eVli-tstM5E")
    # client.apiShutdown() 

    relatedIDs = ytd.randomYoutubeID("fcfQkxwz4Oo")
    for id in relatedIDs: 
        ytd.downloadCaptions("id")

if __name__ == "__main__":
    main()
