import os
import sys
import woc_utils as wu
from sentence_transformers import SentenceTransformer
import matplotlib.pyplot as plt

# unused but required import for doing 3d projections with matplotlib < 3.2
import mpl_toolkits.mplot3d  # noqa: F401
from matplotlib import cm
import numpy as np
from sklearn import decomposition

def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().

    source: https://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


chunks = [chunk for chunk in wu.chunker("./captions/l0e9i8zXcIs.txt", 200, 0.5)]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)
pca = decomposition.PCA(n_components = 3)
pca.fit(embeddings)
X = pca.transform(embeddings)
X = X / np.expand_dims(np.linalg.norm(X, axis=1), axis=1)
X_angles = np.arctan2(np.sqrt(X[:, 0]**2 + X[:, 1]**2), X[:, 2])
cmap = cm.viridis
norm = plt.Normalize(X_angles.min(), X_angles.max())


plt.style.use('dark_background')
fig = plt.figure()
ax = plt.axes(projection="3d")
plt.autoscale(axis='z')
origin = np.zeros((len(embeddings)))
ax.quiver(origin, origin, origin ,X[:, 0], X[:, 1], X[:, 2], 
          colors=cmap(norm(X_angles.flatten())), linewidth=2.5, capstyle='round')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], alpha=0)
set_axes_equal(ax)
plt.show()




