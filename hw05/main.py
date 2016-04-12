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
    sphere = []
    torus = []
    box = []
    
    add_sphere(sphere,50,0,-200,40,4)
    add_sphere(sphere,450,0,-200,40,4)
    add_sphere(sphere,250,0,0,40,4)
    add_sphere(sphere,50,0,200,40,4)
    add_sphere(sphere,450,0,200,40,4)

    matrix_mult(make_rotX(90*pi/180.0),sphere)
    matrix_mult(make_translate(0,250,0),sphere)

    add_torus(torus,250,250,0,10,40,4)
    add_torus(torus,250,250,0,10,70,4)
    add_torus(torus,250,250,0,10,100,4)
    
    matrix_mult(make_rotX(90*pi/180.0),torus)
    matrix_mult(make_scale(2,2,1),torus)
    matrix_mult(make_translate(-250,250,0),torus)
    
    donut = []
    donut += torus
    donut += sphere

    draw_polygons(donut,screen,color)
    
    display(screen)
    
