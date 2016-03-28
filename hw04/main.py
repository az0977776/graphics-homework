from display import *
from draw import *
from parser import *
from matrix import *
import sys

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

add_sphere(edges,100,100,0,50,0.01)
#add_torus(edges,100,100,0,50,150,0.01)
#add_box(edges,150,150,0,50,100,25)
draw_lines(edges,screen,color)


display(screen)

#if len(sys.argv) == 2:
#    f = open(sys.argv[1])

#parse_file( f, edges, transform, screen, color )
#f.close()
