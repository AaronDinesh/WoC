import pyray as pr
import numpy as np
import random

pr.init_window(800, 450, "Hello Pyray")
pr.set_target_fps(60)

NUM_SPHERES = 1000
SCALE = 100


def main():
        
    DRAW_INSTANCED = True
    camera = pr.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)
          

    if not DRAW_INSTANCED:
        draw_loop = DrawSphere()
    else:
        draw_loop = DrawSphereInstanced()



    while not pr.window_should_close():
        pr.update_camera(camera, pr.CAMERA_FREE)
        pr.begin_drawing()
    
        pr.clear_background(pr.BLACK)
    
        pr.begin_mode_3d(camera)
        pr.draw_grid(50, 10.0)
        draw_loop()
            
        pr.end_mode_3d()
    
        pr.end_drawing()
        pr.draw_fps(10,10)
    pr.close_window()


def DrawSphere():
    objects_coords = np.random.random((NUM_SPHERES,3))
    objects_colors = objects_coords * 255

    objects_coords *= SCALE
    objects_colors = np.concatenate([objects_colors, np.ones((NUM_SPHERES, 1))*255], axis=1).astype(np.int32)
    
    def draw_loop():
        for i, _ in enumerate(objects_coords):
            pr.draw_sphere(objects_coords[i].tolist(), 1.0, objects_colors[i].tolist())
    return draw_loop

def DrawSphereInstanced():
    INSTANCES = 1000
    transforms = []
    

    for i in range(1000):
        transforms.append(pr.matrix_translate(random.random()*100, random.random()*100, random.random()*100))


    circleMesh = pr.gen_mesh_sphere(1.0, 8, 8)
    circleMaterial = pr.load_material_default()
    
    def draw_loop():
        pr.draw_mesh_instanced(circleMesh, circleMaterial, transforms, INSTANCES)

    return draw_loop

if __name__ == '__main__':
    main()
