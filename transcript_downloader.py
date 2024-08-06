import networkx as nx
import woc_utils as wu
import youtubeData as ytd
import fnmatch
import os
import numpy as np
import time
from multiprocessing import Process, Array, Value

def manager(worker_thread_done, work_pool, done) -> None:
    while done.value != 1:
        while len(fnmatch.filter(os.listdir('captions/'), '*.txt')) < 100:
            for i in range(len(work_pool)):
                
                # If the thread has no work. Give it work
                if worker_thread_done[i] == 1:

                    new_work = ytd.generateRandomYoutubeID(work_pool[i].value.decode('utf-8'))
                    
                    # All Youtube IDs seem to be 11 chars long. Since we are dealing with fixed size arrays, I assert to enforce this.
                    assert len(new_work) == 11, "Youtube ID is not 11 chars long"
                    
                    # Make sure the work is unique
                    while os.path.exists(f"captions/{new_work}.txt") and new_work in [x.value.decode('utf-8') for x in work_pool]:
                        new_work = ytd.generateRandomYoutubeID(new_work)

                    work_pool[i].value = new_work.encode('utf-8')

                    worker_thread_done[i] = 0
                        

            # Wait until one of the treads is finished
            while not np.all(worker_thread_done):
                time.sleep(0.001)
        
        done.value = 1
        print("Manager is gracefully exiting")

def manager_test(worker_thread_done, work_pool, done) -> None:
    from string import ascii_lowercase

    idx = 0
    while done.value != 1:
        while idx < 100:
            for i in range(len(work_pool)):
                if worker_thread_done[i] == 1:
                    new_work = "".join(np.random.choice(list(ascii_lowercase), 11))

                    if(new_work not in [x for x in work_pool]):
                        # If the thread has no work. Give it some work
                        print(f"Work for thread id {i} is {new_work}")
                        work_pool[i].value = new_work.encode('utf-8')
                        print(work_pool[i].value.decode('utf-8'))
                        worker_thread_done[i] = 0

            # Assign work and then wait until one of the treads is finished
            while not np.all(worker_thread_done):
                time.sleep(0.001)
            
            idx += 1
        done.value = 1
       
        print("Manager is gracefully exiting")

def worker_thread(worker_thread_done, work_pool, thread_id, done) -> None:
    print(f"Hello from Thread {thread_id}")
    while done.value != 1:
        print(f"Thread {thread_id}: My work is {work_pool[thread_id].value}")
        ytd.downloadCaptions(work_pool[thread_id].value.decode('utf-8'))
        worker_thread_done[thread_id] = 1
        print(f"Thread {thread_id}: Finished {work_pool[thread_id].value}. Waiting for new work...")

        while worker_thread_done[thread_id] == 1:
            time.sleep(0.001)
            if done.value == 1:
                break

    print(f"Thread {thread_id} is gracefully exiting.")


def main():
    # wu.chunker("test.txt")

    # client = youtubeAPI(client_secret_file="client_secret.json")
    # ret = client.authenticate()
    # client.downloadCaptions("eVli-tstM5E")
    # client.apiShutdown()
    
    start = time.time()
    processes = []
    
    # 'Array' does do some locking in the background
    # Maybe change it to RawArray and do the locking ourself?
    worker_thread_done = Array('i', [0, 0, 0, 0])
    work_pool = [Array('c', 11) for _ in range(4)] 
    
    # Initalize the work pool
    work_pool[0].value = "l0e9i8zXcIs".encode('utf-8') 
    work_pool[1].value = "kTMEXgxtE4s".encode('utf-8') 
    work_pool[2].value = "ShmVne51sF4".encode('utf-8') 
    work_pool[3].value = "zabpcOP7H3U".encode('utf-8')

    done = Value('i', 0) 
    manager_thread = Process(target=manager, args=(worker_thread_done, work_pool, done,))
    manager_thread.start()
    for i in range(4):
        processes.append(Process(target=worker_thread, args=(worker_thread_done, work_pool, i, done,)))
        processes[i].start()
    

    manager_thread.join()
    for p in processes:
        p.join()
    
    print(f"Time taken: {time.time()-start}")


if __name__ == "__main__":
    main()
