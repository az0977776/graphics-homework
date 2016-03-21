from display import *
from draw import *
from matrix import *
from random import *

screen = new_screen()

def randColor():
    return [randint(0,255),randint(0,255),randint(0,255)]

matt = []
add_edge(matt, 100, 100, 0, 200, 150, 0)
add_edge(matt, 200, 150, 0, 100, 200, 0)
add_edge(matt, 200, 100, 0, 100, 150, 0)
add_edge(matt, 100, 150, 0, 200, 200, 0)
add_edge(matt, 100, 100, 0, 150, 200, 0)
add_edge(matt, 150, 200, 0, 200, 100, 0)
add_edge(matt, 100, 200, 0, 150, 100, 0)
add_edge(matt, 150, 100, 0, 200, 200, 0)

make_translate(matt,-50,-50,0)
for tally in range(100):
    for mark in range(12):
        make_rotZ(matt,30)
        make_translate(matt,250,500-tally,0)
        make_rotX(matt,60)
        draw_lines(matt,screen, [0,tally*2,0])    
        make_rotX(matt,-60)
        make_translate(matt,-250,-500+tally,0)

display(screen)
display(screen)
