from display import *
from draw import *
from parser import *
from matrix import *
import sys

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

if len(sys.argv) == 2:
    f = open(sys.argv[1])

    parse_file( f, edges, transform, screen, color )
    f.close()

else:
    a = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [250.0, 250.0, 0.0, 1]]
    b = [[0,0,0,1]]
    matrix_mult(a,b)
    print b
