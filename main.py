from pydoc import cli
import networkx as nx
from youtubeAPI import youtubeAPI
import woc_utils as wu
import transcriptYoutubeAPI as tya

def main():
    # wu.chunker("test.txt")

    # client = youtubeAPI(client_secret_file="client_secret.json")
    # ret = client.authenticate()
    # client.downloadCaptions("eVli-tstM5E")
    # client.apiShutdown() 

    tya.downloadCaptions("eVli-tstM5E")

if __name__ == "__main__":
    main()
