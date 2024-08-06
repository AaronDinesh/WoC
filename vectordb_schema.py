from docarray import BaseDoc
from docarray.typing import NdArray

class wocSchema(BaseDoc):
    id: str = ''
    embedding: NdArray[384]
