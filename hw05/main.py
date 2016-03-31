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

#add_polygon(edges,100,100,0,200,100,0,100,200,0)
#add_polygon(edges,300,300,0,300,400,0,400,400,0)
add_box(edges,100,100,100,100,150,200)
print_matrix(edges)
matrix_mult(make_translate(50,50,50),edges)
matrix_mult(make_rotY(30.0/180*pi),edges)
draw_polygons(edges,screen,color)

display(screen)


# if len(sys.argv) == 2:
#     f = open(sys.argv[1])

# parse_file( f, edges, transform, screen, color )
# f.close()
