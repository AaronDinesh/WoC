from docarray import DocList
import numpy as np
from vectordb import InMemoryExactNNVectorDB, HNSWVectorDB
from docarray import BaseDoc
from docarray.typing import NdArray

class ToyDoc(BaseDoc):
  text: str = ''
  embedding: NdArray[128]



# Specify your workspace path
db = InMemoryExactNNVectorDB[ToyDoc](workspace='./database')

# Index a list of documents with random embeddings
doc_list = [ToyDoc(text=f'toy doc {i}', embedding=np.random.rand(128)) for i in range(1000)]
db.index(inputs=DocList[ToyDoc](doc_list))

with db.serve(protocol='grpc', port=1234 ,replicas=1, shards=1) as service:
    service.block()


