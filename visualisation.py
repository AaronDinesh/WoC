from mayavi import mlab
import numpy as np
import woc_utils as wu
from sentence_transformers import SentenceTransformer
from sklearn import decomposition
from os import listdir 

class visualAPI:
    def __init__(self) -> None:
        self.bubbles = None
        self.x = None
        self.y = None
        self.z = None
        self.value = None
        self.files = listdir("./captions/")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
    def setup(self)-> None:
        # Clear the figure
        mlab.clf()

        self.x, self.y, self.z, self.value = np.zeros((4, 1))
        self.bubbles = mlab.points3d(self.x, self.y, self.z, self.value)

    @mlab.animate(delay=100)
    def anim(self) -> None:

        for file in self.files:
            embedding = np.array(self.model.encode([chunk for chunk in wu.chunker(f"./captions/{file}", 5, 0.5)]))
            pca = decomposition.PCA(n_components = 4)
            pca.fit(embedding)
            X = pca.transform(embedding).mean(axis=0)

            self.x = np.concatenate([self.x, np.expand_dims(X[0], axis=0)], axis=0)
            self.y = np.concatenate([self.y, np.expand_dims(X[1], axis=0)], axis=0)
            self.z = np.concatenate([self.z, np.expand_dims(X[2], axis=0)], axis=0)
            self.value = np.concatenate([self.value, np.expand_dims(X[3], axis=0)], axis=0)
            self.bubbles.mlab_source.reset(x=self.x, y=self.y, z=self.z, scalars=self.value)
            # arms.mlab_source.reset(x=x, y=y, z=z, scalars=value)
            yield

    def runVisual(self) -> None:
        self.setup()
        self.anim()
        mlab.show()

    
# global bubbles

# # Clear the figure
# mlab.clf()

# def setup():
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
