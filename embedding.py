import os
import woc_utils as wu
from sentence_transformers import SentenceTransformer
import numpy as np
from tqdm import tqdm
import json
from multiprocessing import Process, Queue, cpu_count
import time

def split_files(files:list[str], n:int) ->list[list[str]]:
    length = len(files)
    chunk_size = length // n
    remainder = length % n  
    
    result = []
    start = 0

    for i in tqdm(range(n), desc="Spliting files for threads"):
        end = start + chunk_size + (1 if remainder else 0)
        result.append(files[start:end])
        start = end

    return result

def embed_files_threaded(data:tuple[id:int, list[str]], completed_queue):
    id = data[0]
    files = data[1]
    print(f"Thread {id}: Starting...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embedding_dict = {}
    for file in files:
        chunks = [chunk for chunk in wu.chunker(f"./captions/{file}", 200, 0.5)]
        embedding = np.array(model.encode(chunks))
        # -4 so that we strip the .txt, leaving just the video id 
        embedding_dict[file[:-4]] = embedding.mean(axis=0).tolist()
    print(f"Thread {id}: Completed work. Exiting...")
    completed_queue.put(embedding_dict)



if __name__ == "__main__":
    embeddings_dict = {}
    NUM_WORKERS = cpu_count()
    print(f"Using {NUM_WORKERS} processes...")
    split_files = split_files(os.listdir("./captions"), NUM_WORKERS)

    completed_queue = Queue()
    processes = []
    start = time.time()
    for i in enumerate(split_files):
        p = Process(target=embed_files_threaded, args=(i, completed_queue,))
        p.start()
        processes.append(p)
    
    for p in processes:
        embeddings_dict.update(completed_queue.get())

    for p in processes:
        p.join()
    print(f"Threaded Time: {time.time()-start}")

    with open("./WoC Unity/Assets/StreamingAssets/embeddings.json", "w") as f:
        json.dump(embeddings_dict, f)

