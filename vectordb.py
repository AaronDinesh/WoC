from docarray import BaseDoc
from docarray.typing import NdArray
from vectordb import InMemeoryExactNNVectorDB

class wocSchema(BaseDoc):
    id: str = ''
    embedding: NdArray[384]

db = InMemoryExactNNVectorDB[wocSchema](workspace='./database')

with db.serve(protocol='grpc', port=1234, replicas=1, shard=1) as service:
    service.block()


