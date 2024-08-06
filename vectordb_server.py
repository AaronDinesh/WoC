from vectordb import InMemoryExactNNVectorDB
from vectordb_schema import wocSchema
from docarray import DocList
import numpy as np

db = InMemoryExactNNVectorDB[wocSchema](workspace='./database')

doc_list = [wocSchema(id=f'toy doc {i}', embedding=np.random.rand(384)) for i in range(1000)]
db.index(inputs=DocList[wocSchema](doc_list))

with db.serve(protocol='grpc', port=1234, replicas=1, shards=1) as service:
    service.block()


