from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]

matt = []
add_edge(matt, 100, 100, 0, 200, 100, 0)
add_edge(matt, 200, 100, 0, 200, 200, 0)
add_edge(matt, 200, 200, 0, 100, 200, 0)
add_edge(matt, 100, 100, 0, 100, 200, 0)
draw_lines(matt, screen, color)

make_translate(matt,50,50,50)
draw_lines(matt,screen, color)

make_translate(matt,200,0,0)
draw_lines(matt,screen,color)

make_rotX(matt,60)
draw_lines(matt,screen,color)

display(screen)
