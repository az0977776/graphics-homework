from display import *
from matrix import *
from draw import *

def parseArgs(array):
    temp = array.split(" ")
    for mark in range(len(temp)):
        temp[mark] = float(temp[mark])
    return temp

def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r", 1)
    buffer = f.read()
    buffer = buffer.split("\n")
    print buffer
    index = 0
    while (index < len(buffer)):
        if (buffer[index] == "line"):
            temp = parseArgs(buffer[index+1])
            add_edge(points,temp[0],temp[1],temp[2],temp[3],temp[4],temp[5])
            index+=2
        elif (buffer[index] == "circle"):
            index+=2
        elif (buffer[index] == "hermite"):
            index+=2
        elif (buffer[index] == "bezier"):
            index+=2
        elif (buffer[index] == "ident"):
            ident(transform)
            index+=1
        elif (buffer[index] == "scale"):
            temp = parseArgs(buffer[index+1])
            transform = make_scale(temp[0],temp[1],temp[2])
            index+=2
        elif (buffer[index] == "translate"):
            temp = parseArgs(buffer[index+1])
            transform = make_translate(temp[0],temp[1],temp[2])                
            index+=2
        elif (buffer[index] == "xrotate"):
            temp = parseArgs(buffer[index+1])
            transform = make_rotX(temp[0])
            index+=2
        elif (buffer[index] == "yrotate"):
            temp = parseArgs(buffer[index+1])
            transform = make_rotY(temp[0])
            index+=2
        elif (buffer[index] == "zrotate"):
            temp = parseArgs(buffer[index+1])
            transform = make_rotZ(temp[0])
            index+=2
        elif (buffer[index] == "apply"):
            matrix_mult(transform,points)
            index+=1
        elif (buffer[index] == "display"):
            draw_lines(points,screen,color)
            display(screen)
            index+=1
        elif (buffer[index] == "save"):
            save_extension(screen,'pic.ppm')
            index+=1
        elif (buffer[index] == "quit"):
            index+=1
        else:
            index+=1
            

