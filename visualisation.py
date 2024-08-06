# # Create the data.
# from numpy import pi, sin, cos, mgrid
# dphi, dtheta = pi/250.0, pi/250.0
# [phi,theta] = mgrid[0:pi+dphi*1.5:dphi,0:2*pi+dtheta*1.5:dtheta]
# m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
# r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
# x = r*sin(phi)*cos(theta)
# y = r*cos(phi)
# z = r*sin(phi)*sin(theta)

# # View it.
# from mayavi import mlab
# s = mlab.mesh(x, y, z)
# mlab.show()



from mayavi import mlab
import numpy as np
import time

mlab.clf()  # Clear the figure

# t = np.linspace(0, 20, 200)
# swirl = mlab.plot3d(np.sin(t), np.sin(t), 0.1*t, t)

# x, y, z, value = np.random.random((4, 1))
# bubbles = mlab.points3d(x, y, z, value)


# mlab.show()




@mlab.animate(delay=100)
def anim():
    x, y, z, value = np.random.random((4, 1))
    bubbles = mlab.points3d(x, y, z, value)

    for i in range (1000):
        (x, y, z, value) = [np.concatenate([i, np.random.random((1,))], axis=0) for i in (x, y, z, value)]
        bubbles.mlab_source.reset(x=x, y=y, z=z, scalars=value)
        yield


anim()
mlab.show()
