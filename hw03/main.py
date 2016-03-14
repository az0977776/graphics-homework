from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

add_circle(edges,250,250,0,50,0.01)
print_matrix(edges)

draw_lines(edges,screen,color)
display(screen)

#parse_file( 'script_nocurves', edges, transform, screen, color )
