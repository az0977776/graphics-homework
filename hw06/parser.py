from display import *
from matrix import *
from draw import *
import sys
import math

ARG_COMMANDS = [ 'line', 'scale', 'translate', 'xrotate', 'yrotate', 'zrotate', 'circle', 'bezier', 'hermite', 'sphere', 'box', 'torus']

def parse_file( f, points, transform, screen, color ):

    stack = []
    
    n = new_matrix()
    ident(n)
    stack += [n]
     
    commands = f.readlines()

    c = 0
    while c  <  len(commands):
        cmd = commands[c].strip()
        if cmd in ARG_COMMANDS:
            c+= 1
            args = commands[c].strip().split(' ')
            i = 0
            while i < len( args ):
                args[i] = float( args[i] )
                i+= 1

            if cmd == 'line':
                edge = []
                add_edge( edge, args[0], args[1], args[2], args[3], args[4], args[5] )
                matrix_mult( stack[-1], edge)
                draw_lines( edge, screen, color)
                
            elif cmd == 'circle':
                edge = []
                add_circle( edge, args[0], args[1], 0, args[2], .01 )
                matrix_mult( stack[-1], edge)
                draw_lines( edge, screen, color)
                
            elif cmd == 'bezier':
                edge = []
                add_curve( edge, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'bezier' )
                matrix_mult( stack[-1], edge)
                draw_lines( edge, screen, color)
                
            elif cmd == 'hermite':
                edge = []
                add_curve( edge, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'hermite' )
                matrix_mult( stack[-1], edge)
                draw_lines( edge, screen, color)
                
            elif cmd == 'sphere':
                polygon = []
                add_sphere( polygon, args[0], args[1], 0, args[2], 5 )
                matrix_mult( stack[-1], polygon)
                draw_polygons( polygon, screen, color)
                
            elif cmd == 'torus':
                polygon = []
                add_torus( polygon, args[0], args[1], 0, args[2], args[3], 5 )
                matrix_mult( stack[-1], polygon)
                draw_polygons( polygon, screen, color)
                
            elif cmd == 'box':
                polygon = []
                add_box( polygon, args[0], args[1], args[2], args[3], args[4], args[5] )
                matrix_mult( stack[-1], polygon)
                draw_polygons( polygon, screen, color)

            elif cmd == 'scale':
                s = make_scale( args[0], args[1], args[2] )
                matrix_mult( stack[-1], s)
                stack[-1] = s

            elif cmd == 'translate':
                t = make_translate( args[0], args[1], args[2] )
                matrix_mult( stack[-1], t)
                stack[-1] = t

            else:
                angle = args[0] * ( math.pi / 180 )
                if cmd == 'xrotate':
                    r = make_rotX( angle )
                elif cmd == 'yrotate':
                    r = make_rotY( angle )
                elif cmd == 'zrotate':
                    r = make_rotZ( angle )
                matrix_mult( stack[-1] , r)
                stack[-1] = r

        elif cmd == 'push':
            stack.append(stack[-1])

        elif cmd == 'pop':
            stack.pop()
            
        elif cmd == 'ident':
            ident( stack[-1] )
            
        elif cmd == 'apply':
            matrix_mult( stack[-1], points )

        elif cmd == 'clear':
            points = []

        elif cmd in ['display', 'save' ]:
            #screen = new_screen()
            #draw_polygons( points, screen, color )
            
            if cmd == 'display':
                display( screen )

            elif cmd == 'save':
                c+= 1
                save_extension( screen, commands[c].strip() )
        elif cmd == 'quit':
            return    
        elif cmd[0] != '#':
            print 'Invalid command: ' + cmd
        c+= 1

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

if len(sys.argv) == 2:
    f = open(sys.argv[1])

    parse_file( f, edges, transform, screen, color )
    f.close()
