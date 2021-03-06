import math

def make_bezier():
    t = new_matrix()
    t[0][0] = -1
    t[0][1] = 3
    t[0][2] = -3
    t[0][3] = 1
    t[1][0] = 3
    t[1][1] = -6
    t[1][2] = 3
    t[2][0] = -3
    t[2][1] = 3
    t[3][0] = 1
    return t

def make_hermite():
    t = new_matrix()
    t[0][0] = 2
    t[0][1] = -3
    t[0][2] = 0
    t[0][3] = 1
    t[1][0] = -2
    t[1][1] = 3
    t[2][0] = 1
    t[2][1] = -2
    t[2][2] = 1
    t[3][0] = 1
    t[3][1] = -1
    return t

def generate_curve_coefs( p1, p2, p3, p4, t ):
    m = [[p1[0], p2[0], p3[0], p4[0]],
         [p1[1], p2[1], p3[1], p4[1]]]
    matrix_mult(t, m)
    return m    

def make_translate( x, y, z ):
    t = new_matrix()
    ident(t)
    t[3][0] = x
    t[3][1] = y
    t[3][2] = z
    return t

def make_scale( x, y, z ):
    s = new_matrix()
    ident(s)
    s[0][0] = x
    s[1][1] = y
    s[2][2] = z
    return s
    
def make_rotX( theta ):    
    theta = math.pi*theta/180
    rx = new_matrix()
    ident( rx )
    rx[1][1] = math.cos( theta )
    rx[2][1] = -1 * math.sin( theta )
    rx[1][2] = math.sin( theta )
    rx[2][2] = math.cos( theta )
    return rx

def make_rotY( theta ):
    theta = math.pi*theta/180
    ry = new_matrix()
    ident( ry )
    ry[0][0] = math.cos( theta )
    ry[2][0] = -1 * math.sin( theta )
    ry[0][2] = math.sin( theta )
    ry[2][2] = math.cos( theta )
    return ry

def make_rotZ( theta ):
    theta = math.pi*theta/180
    rz = new_matrix()
    ident( rz )
    rz[0][0] = math.cos( theta )
    rz[1][0] = -1 * math.sin( theta )
    rz[0][1] = math.sin( theta )
    rz[1][1] = math.cos( theta )
    return rz

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len( matrix ) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, x ):
    for r in range( len( matrix[0] ) ):
        for c in range( len( matrix ) ):
            matrix[c][r] *= x

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    
    t = new_matrix( 4, 1 )

    for c in range( len( m2 ) ):        
        
        for r in range(4):
            t[0][r] = m2[c][r]
            
        for r in range(4):
            m2[c][r] = m1[0][r] * t[0][0] + m1[1][r] * t[0][1] + m1[2][r] * t[0][2] + m1[3][r] * t[0][3]


