from math import *

def make_translate( matrix, x, y, z ):
    c = new_matrix()
    c = ident(c)
    c[0][3] = x
    c[1][3] = y
    c[2][3] = z
    for mat in range(len(matrix)):
        matrix[mat] = matrix_mult(c,matrix[mat])
    
def make_scale( matrix, x, y, z ):
    c = new_matrix()
    c = ident(c)
    c[0][0] = x
    c[1][1] = y
    c[2][2] = z
    for mat in range(len(matrix)):
        matrix[mat] = matrix_mult(c,matrix[mat])
    
def make_rotX( matrix, theta ):
    theta = pi*theta/180
    c = new_matrix()
    c[0][0] = 1
    c[3][3] = 1
    c[1][1] = cos(theta)
    c[1][2] = -1*sin(theta)
    c[2][1] = sin(theta)
    c[2][2] = cos(theta)
    for mat in range(len(matrix)):
        matrix[mat] = matrix_mult(c,matrix[mat])
    
    
def make_rotY( matrix, theta ):
    theta = pi*theta/180
    c = new_matrix()
    c[0][0] = cos(theta)
    c[0][2] = -1*sin(theta)
    c[1][1] = 1
    c[2][0] = sin(theta)
    c[2][2] = cos(theta)
    c[3][3] = 1
    for mat in range(len(matrix)):
        matrix[mat] = matrix_mult(c,matrix[mat])

def make_rotZ( matrix, theta ):
    theta = pi*theta/180
    c = new_matrix()
    c[0][0] = cos(theta)
    c[0][1] = -1*sin(theta)
    c[1][0] = sin(theta)
    c[1][1] = cos(theta)
    c[2][2] = 1
    c[3][3] = 1
    for mat in range(len(matrix)):
        matrix[mat] = matrix_mult(c,matrix[mat])

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    for mark in range(len(matrix)):
        print matrix[mark]

def ident( matrix ):
    matrix = new_matrix()
    for counter in range(4):
        matrix[counter][counter] = 1
    return matrix

def scalar_mult( matrix, x ):
    for tally in 3:
        for mark in range(len(matrix[0])):
            matrix[tally][mark] *= x;

#m1 * m2 -> m2
def matrix_mult( trans, matt ):
    m3 = [0,0,0,0]
    for mark in range(len(trans)):
        for tally in range(len(trans[0])):
            m3[mark] = m3[mark] + trans[mark][tally] * matt[tally]
    return m3

