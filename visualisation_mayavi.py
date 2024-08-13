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
        np.random.seed(0)
        self.files = listdir("./captions/")
        self.figure = mlab.figure(figure='Visualizer', bgcolor=self.rgb2unit((0, 0, 0)), fgcolor=self.rgb2unit((255, 255, 255)))
        self.coords = np.random.random((len(self.files), 3))
        self.colors = np.random.random(len(self.files))
        self.bubbles = mlab.points3d(self.coords[:, 0], self.coords[:, 1], self.coords[:, 2])
        self.bubbles.glyph.scale_mode = 'scale_by_vector'
        self.bubbles.mlab_source.dataset.point_data.scalars = self.colors
        # self.model = SentenceTransformer("all-MiniLM-L6-v2")
    def rgb2unit(self, rgb: tuple[int, int, int]) -> tuple[float, float, float]:
        return tuple(x / 255 for x in rgb)

    def unit2rgb(self, unit: tuple[float, float, float]) -> tuple[int, int, int]:
        return tuple(int(x * 255) for x in unit)

    def setup(self)-> None:
        # Clear the figure
        mlab.clf()

        self.x, self.y, self.z, self.value = np.ones((4, 1))
        self.bubbles = mlab.points3d(self.x, self.y, self.z, self.value)

    def __anim(self) -> None:
        bubbles = self.bubbles
        coords = self.coords
        velocity = np.random.random(self.coords.shape)
        @mlab.animate(delay=100)
        def animate(coords=coords, bubbles=bubbles, velocity=velocity):
            iter = 0
            while 1:
                coords += np.where(coords > 10.0, -1, 1) * velocity / 10
                bubbles.mlab_source.points = coords
                mlab.gcf().scene.render()
                print(f"Iteration: {iter}")
                iter += 1
                # arms.mlab_source.reset(x=x, y=y, z=z, scalars=value)
                # print(x, y, z, value)
                yield

        return animate

    def runVisual(self) -> None:
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