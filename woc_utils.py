import numpy as np
import string

# A simple sliding window buffer. Impliments and iterator interface.
class windowedBuffer:
    def __init__(self, window_size: int = 1):
        self.buffer = []
        self.window_size = window_size

    def clear(self):
        self.buffer.clear()
    
    def append(self, item):
        if len(self.buffer) + 1 > self.window_size:
            self.buffer[:-1] = self.buffer[1:]
            self.buffer[-1] = item
        else:
            self.buffer.append(item)
    
    def __len__(self):
        return len(self.buffer)

    def __iter__(self):
        self.idx = 0
        return self
    
    def __next__(self):
        if(self.idx + 1 < len(self.buffer)):
            self.idx += 1
            return self.buffer[self.idx]
        else:
            raise StopIteration
        

# Accepts a text file and splits it into chunks of "chunk_limits" with an overlap of chunk_overlap
# e.g. A chunk_overlap of 0.5 would mean 50% overlap with the previous chunk
def chunker(filepath: str, chunk_limit: int = 0, chunk_overlap: float = 0) -> list[str]:
    buffer = windowedBuffer(chunk_limit)
    text_overlap = int(chunk_limit*chunk_overlap)
    inserted_words = 0
    
    with open(filepath, 'r') as f:
        for line in f:
            for word in line.split():
                buffer.append(word)
                inserted_words += 1
                
                if inserted_words > chunk_limit:
                    if inserted_words % text_overlap == 0:
                        yield " ".join(iter(buffer))
                else:
                    if inserted_words % chunk_limit == 0:
                        yield " ".join(iter(buffer))
        
        yield " ".join(buffer)
        
