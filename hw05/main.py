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

add_sphere(edges,100,100,0,50,5)
#print edges

#matrix_mult(make_rotX(45.0/180*pi),edges)
#matrix_mult(make_rotY(45.0/180*pi),edges)

matrix_mult(make_scale(3,3,3),edges)
matrix_mult(make_translate(100,0,0),edges)

#print_matrix(edges)
draw_polygons(edges,screen,color)

display(screen)


# if len(sys.argv) == 2:
#     f = open(sys.argv[1])
# parse_file( f, edges, transform, screen, color )
# f.close()
