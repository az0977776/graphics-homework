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
            print "drawing line"
            temp = parseArgs(buffer[index+1])
            add_edge(points,temp[0],temp[1],temp[2],temp[3],temp[4],temp[5])
            index+=2
        elif (buffer[index] == "circle"):
            print "drawing circle"
            temp = parseArgs(buffer[index+1])
            add_circle(points,temp[0],temp[1],0,temp[3],0.001)
            index+=2
        elif (buffer[index] == "hermite"):
            print "drawing hermite"
            temp = parseArgs(buffer[index+1])
            add_curve(points,temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],0.001,"h")
            index+=2
        elif (buffer[index] == "bezier"):
            temp = parseArgs(buffer[index+1])
            add_curve(points,temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],0.001,"b")
            index+=2
        elif (buffer[index] == "ident"):
            ident(transform)
            index+=1
        elif (buffer[index] == "scale"):
            print "scaling"
            temp = parseArgs(buffer[index+1])
            transform = make_scale(temp[0],temp[1],temp[2])
            index+=2
        elif (buffer[index] == "translate"):
            print "translating"
            temp = parseArgs(buffer[index+1])
            transform = make_translate(temp[0],temp[1],temp[2])                
            index+=2
        elif (buffer[index] == "xrotate"):
            print "xrot"
            temp = parseArgs(buffer[index+1])
            transform = make_rotX(temp[0])
            index+=2
        elif (buffer[index] == "yrotate"):
            print "yrot"
            temp = parseArgs(buffer[index+1])
            transform = make_rotY(temp[0])
            index+=2
        elif (buffer[index] == "zrotate"):
            print "zrot"
            temp = parseArgs(buffer[index+1])
            transform = make_rotZ(temp[0])
            index+=2
        elif (buffer[index] == "apply"):
            print "apply"
            matrix_mult(transform,points)
            index+=1
        elif (buffer[index] == "display"):
            print "displaying"
            draw_lines(points,screen,color)
            display(screen)
            index+=1
        elif (buffer[index] == "save"):
            draw_lines(points,screen,color)
            save_ppm(screen,temp[0])
            index+=1
        else:
            index+=1
            

