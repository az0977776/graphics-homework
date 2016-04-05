from display import *
from draw import *
from parser import *
from matrix import *
from math import *
import sys

if len(sys.argv) == 2:
    f = open(sys.argv[1])
    parse_file( f, edges, transform, screen, color )
    f.close()

else:
    screen = new_screen()
    color = [ 0, 255, 0 ]
    edges = []
    transform = new_matrix()

    #add_sphere(edges,250,250,0,40,2)
    #add_torus(edges,250,250,0,10,100,2)
    
    sphere = []
    torus = []
    box = []
    
    add_sphere(sphere,20,100,0,15,5)
    add_sphere(sphere,150,100,0,20,5)
    add_sphere(sphere,280,100,0,15,5)
    
    add_torus(torus,20,100,0,12,75,5)
    add_torus(torus,150,100,0,15,100,5)
    add_torus(torus,280,100,0,12,75,5)
    
    donut = []
    donut += torus 
    donut += sphere
    matrix_mult(make_rotX(90),donut)
    #matrix_mult(make_rotY(30),donut)
    matrix_mult(make_translate(150,150,0),donut)
    
    draw_polygons(donut,screen,color)
    
    display(screen)


