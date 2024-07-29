import networkx as nx
import woc_utils as wu
import youtubeData as ytd
import fnmatch
import os
import numpy as np
import time
from multiprocessing import Process, Array
from ctypes import c_char_p

work_pool = []
worker_thread_done = [True, True, True, True]

def manager(worker_thread_done, work_pool) -> None:
    done = False
    
    while not done:
        while len(fnmatch.filter(os.listdir('captions/'), '*.txt')) < 100:
            for i in range(len(work_pool)):
                if worker_thread_done[i] == 1:
                    new_work = ytd.randomYoutubeID(work_pool[i])

                    if(not os.path.exists(f"captions/{new_work}.txt") and new_work not in work_pool.to_list()):
                        # If the thread has no work. Give it some work
                        work_pool[i] = (new_work).encode('utf-8')
                        worker_thread_done[i] = 0

            # Assign work and then wait until one of the treads is finished
            while not np.all(worker_thread_done):
                time.sleep(0.001)
        
        done = True


def worker_thread(worker_thread_done, work_pool, thread_id) -> None:
    while worker_thread_done[thread_id] == 1:
        time.sleep(0.001)
    
    ytd.downloadCaptions(work_pool[thread_id].decode('utf-8'))
    
    print(f"Hello from worker: {thread_id}. My work is {work_pool[thread_id].decode('utf-8')}")

    worker_thread_done[thread_id] = 1


def main():
    # wu.chunker("test.txt")

    # client = youtubeAPI(client_secret_file="client_secret.json")
    # ret = client.authenticate()
    # client.downloadCaptions("eVli-tstM5E")
    # client.apiShutdown()

    processes = []
    worker_thread_done = Array('i', [0, 0, 0, 0])
    work_pool = Array(c_char_p, 4) 
    work_pool[:] = [b"xxx",b"xxx",b"xxx",b"xxx"]
    for i in range(4):
        processes.append(Process(target=worker_thread, args=(worker_thread_done, work_pool, i,)))
        processes[i].start()
    

    for p in processes:
        p.join()
    
    for res in worker_thread_done:
        print(res)
        
    return 0

    start = time.time()
    
    next_id = "A5w-dEgIU1M"
    
    while len(fnmatch.filter(os.listdir('captions/'), '*.txt')) < 100:
        if(not os.path.exists(f"captions/{next_id}.txt")):
            ytd.downloadCaptions(next_id)
        else:
            print(f"ID: {next_id} exists. Skipping...")

        relatedIDs = ytd.randomYoutubeID(next_id)
        np.concatenate((relatedIDs, ytd.randomYoutubeID()), axis=0)
        
        next_id = str(np.random.choice(relatedIDs, 1 ,replace=False)[0])

    end = time.time()
    print(end - start)


if __name__ == "__main__":
    main()
