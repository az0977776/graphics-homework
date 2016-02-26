from display import *
from draw import *
import random
import math

screen = new_screen()
color = [0,255,0]

for x in range(XRES+1):
    red = 125
    green = x%XRES
    blue = (XRES-x)%XRES

    draw_line(screen, x, 0, (x+250)%XRES, YRES, [red,green,blue])
    
display(screen)
