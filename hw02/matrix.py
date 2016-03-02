import math

def make_translate( matrix, x, y, z ):
    c = new_matrix()
    c = ident(c)
    matrix[0][3] = x
    matrix[1][3] = y
    matrix[2][3] = z
    for 
    matrix_mult(c,matrix)
    
def make_scale( matrix, x, y, z ):
    pass
    
def make_rotX( matrix, theta ):
    
    pass

def make_rotY( matrix, theta ):
    pass

def make_rotZ( matrix, theta ):
    pass

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    pass

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
def matrix_mult( m1, m2 ):
    m3 = new_matrix()
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                m3[i][j] += m1[i][k] * m2[k][j]
    return m3

