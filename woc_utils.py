import numpy as np
import string

def chunker(filepath: str, chunk_limit: int = 0, chunk_overlap: float = 0) -> list[str]:
    with open(filepath) as f:
        for line in f:
            for word in line:
                if(word == '\n'):
                    print("Found new line")
    
    return