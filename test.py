from multiprocessing import Process
import youtubeData as ytd

def worker(id, thread_id):
    print(f"Thread {thread_id}: Hello")
    ytd.downloadCaptions(id)
    print(f"Thread {thread_id}: Finished downloading {id}")


def main():
    processes = []

    processes.append(Process(target=worker, args=("l0e9i8zXcIs",0,))) 
    processes.append(Process(target=worker, args=("kTMEXgxtE4s",1,)))
    processes.append(Process(target=worker, args=("ShmVne51sF4",2,)))
    processes.append(Process(target=worker, args=("zabpcOP7H3U",3,)))
    
    for p in processes:
        p.start()

    for p in processes:
        p.join()

if __name__ == '__main__':
    main()

