from display import *
from draw import *
from parser import *
from matrix import *
import sys

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

#sphere = []
#torus = []
#box = []

#add_sphere(sphere,20,100,0,15,0.05)
#add_sphere(sphere,150,100,0,20,0.05)
#add_sphere(sphere,280,100,0,15,0.05)

#add_torus(torus,20,100,0,12,75,0.01)
#add_torus(torus,150,100,0,15,100,0.01)
#add_torus(torus,280,100,0,12,75,0.01)

#donut = []
#donut += torus 
#donut += sphere
#matrix_mult(make_rotX(30),donut)
#matrix_mult(make_rotY(30),donut)
#matrix_mult(make_translate(150,150,0),donut)

#draw_lines(donut,screen,color)

#display(screen)

if len(sys.argv) == 2:
    f = open(sys.argv[1])

parse_file( f, edges, transform, screen, color )
f.close()
