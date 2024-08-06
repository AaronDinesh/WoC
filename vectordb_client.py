from vectordb_schema import wocSchema
from vectordb import Client
from docarray import DocList
import numpy as np

from docarray import BaseDoc
from docarray.typing import NdArray

class ToyDoc(BaseDoc):
  text: str = ''
  embedding: NdArray[128]

client = Client[ToyDoc](address='grpc://172.19.47.205:1234')


query = ToyDoc(text='query', embedding=np.random.rand(128))
results = client.search(inputs=DocList[ToyDoc]([query]), limit=1)
for m in results[0].matches:
  print(m)
