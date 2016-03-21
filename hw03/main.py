from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
shape = []
transform = new_matrix()

add_circle(edges, 250,250,0,50,0.001)
draw_lines(edges,screen,color)
add_circle(edges, 250,250,0,75,0.001)
draw_lines(edges,screen,color)
add_circle(edges, 250,250,0,100,0.001)
draw_lines(edges,screen,color)


for mark in range(5):
    add_curve(shape, 30*mark, 150, 150, 50, 350, 150, 350, 300, 0.001, "b")
    draw_lines(shape,screen,color)
    add_curve(shape, 30*mark, 150, 150, 50, 350, 150, 350, 300, 0.001, "h")
    matrix_mult(make_translate(0,-20,0),shape)
    draw_lines(shape,screen,color)

display(screen)
