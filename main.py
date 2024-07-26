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

    # ytd.downloadCaptions("eVli-tstM5E")
    ytd.randomYoutubeID(1)

if __name__ == "__main__":
    main()
