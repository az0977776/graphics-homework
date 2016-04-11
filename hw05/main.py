from display import *
from draw import *
from parser import *
from matrix import *
from math import *
import sys

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

if len(sys.argv) == 2:
    f = open(sys.argv[1])
    parse_file( f, edges, transform, screen, color )
    f.close()

else:
    # #add_sphere(edges,250,250,0,40,2)
    add_torus(edges,250,250,0,25,60,5)
    
    sphere = []
    torus = []
    box = []
    
    # add_sphere(sphere,20,100,0,15,10)
    # add_sphere(sphere,150,100,0,20,10)
    # add_sphere(sphere,280,100,0,15,10)
    
    # add_torus(torus,20,100,0,12,75,10)
    # add_torus(torus,150,100,0,15,100,10)
    # add_torus(torus,280,100,0,12,75,10)
    
    donut = []
    donut += torus
    donut += sphere
    
    matrix_mult(make_rotX(15*pi/180.0),edges)

    matrix_mult(make_scale(2,2,2),edges)
    matrix_mult(make_translate(-200,-100,0),edges)
    
    draw_polygons(edges,screen,color)
    
    display(screen)
    
