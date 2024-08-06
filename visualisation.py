from mayavi import mlab
import numpy as np
import woc_utils as wu
#from sentence_transformers import SentenceTransformer
#from sklearn import decomposition
from os import listdir 
from functools import partial

# Ideally this would only deal with graphing things.
# But for now it'll be mixed with other stuff
# TODO: Change this to only be graphing
class visualAPI:
    def __init__(self) -> None:
        self.bubbles = None
        self.x = None
        self.y = None
        self.z = None
        self.value = None
        self.files = listdir("./captions/")
        self.figure = mlab.figure('Visualizer')
        # self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def test(self):
        print("Hello from API")
    
    def setup(self)-> None:
        # Clear the figure
        mlab.clf()

        self.x, self.y, self.z, self.value = np.ones((4, 1))
        self.bubbles = mlab.points3d(self.x, self.y, self.z, self.value)

    def __anim(self) -> None:
        files = self.files
        x = self.x
        y = self.y
        z = self.z
        value = self.value
        bubbles = self.bubbles
        
        @mlab.animate(delay=100)
        def animate(files=files,x=x, y=y, z=z, value=value, bubbles=bubbles):
            for file in self.files:
                x = np.concatenate([x, np.random.random((1,))], axis=0)
                y = np.concatenate([y,np.random.random((1,))], axis=0)
                z = np.concatenate([z, np.random.random((1,))], axis=0)
                value = np.concatenate([value, np.random.random((1,))], axis=0)
                bubbles.mlab_source.reset(x=x, y=y, z=z, scalars=value)
                # arms.mlab_source.reset(x=x, y=y, z=z, scalars=value)
                yield

        return animate

    def runVisual(self) -> None:
        self.setup()
        animation = self.__anim()
        animation()
        mlab.show()

    
# global bubbles
# # Clear the figure
# mlab.clf()
# def setup():
#     global bubbles
#     x, y, z, value = np.random.random((4, 2))
#     bubbles = mlab.points3d(x, y, z, value)
#     # arms = mlab.plot3d(x, y, z, value)
#     return x, y, z, value
# @mlab.animate(delay=100)
# def anim(x, y, z, value):
#     for i in range (1000):
#         (x, y, z, value) = [np.concatenate([i, np.random.random((1,))], axis=0) for i in (x, y, z, value)]
#         bubbles.mlab_source.reset(x=x, y=y, z=z, scalars=value)
#         # arms.mlab_source.reset(x=x, y=y, z=z, scalars=value)
#         yield
# x, y, z, value = setup()
# anim(x, y, z, value)
# mlab.show()


viz = visualAPI()
viz.runVisual()
