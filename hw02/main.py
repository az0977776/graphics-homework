from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

matt = [[],[],[],[]]
add_edge(matt, 100, 100, 0, 200, 100, 0)
add_edge(matt, 200, 100, 0, 200, 200, 0)
add_edge(matt, 200, 200, 0, 100, 200, 0)
add_edge(matt, 100, 100, 0, 100, 200, 0)
draw_lines(matt, screen, color)
make_translate(matt,150,150,0)
draw_lines(matt, screen, color)

display(screen)
