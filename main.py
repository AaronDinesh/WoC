from pydoc import cli
import networkx as nx
from youtubeAPI import youtubeAPI
import woc_utils as wu

def main():
    wu.chunker("test.txt")

    # client = youtubeAPI(client_secret_file="client_secret.json")
    # ret = client.authenticate()
    # client.downloadCaptions("dQw4w9WgXcQ")
    # client.apiShutdown() 

if __name__ == "__main__":
    main()
