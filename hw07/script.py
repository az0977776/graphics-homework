import mdl
from display import *
from matrix import *
from draw import *

ARG_COMMANDS = [ 'line', 'scale', 'move', 'rotate', 'circle', 'bezier', 'hermite', 'sphere', 'box', 'torus']

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    stack = []
    stack += [tmp]

    p = mdl.parseFile(filename) 
    p = p[0]
    
    c = 0
    
    # if p:
    #     (commands, symbols) = p
    #     print commands
    #     print symbols
    # else:
    #     print "Parsing failed."
    #     return

    stack = [ tmp ]
    screen = new_screen()
        
    while c < len(p):
        cmd = p[c]
        command = cmd[0]
        if cmd[0] in ARG_COMMANDS:
            args = cmd[1:]
            #print command
            #print args
            if command == 'line':
                edge = []
                add_edge( edge, args[0], args[1], args[2], args[3], args[4], args[5] )
                matrix_mult( stack[-1], edge)
                draw_lines( edge, screen, color)
                           
            elif command == 'circle':
                edge = []
                add_circle( edge, args[0], args[1], 0, args[2], .01 )
                matrix_mult( stack[-1], edge)
                draw_lines( edge, screen, color)
                
            elif command == 'bezier':
                edge = []
                add_curve( edge, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'bezier' )
                matrix_mult( stack[-1], edge)
                draw_lines( edge, screen, color)
                
            elif command == 'hermite':
                edge = []
                add_curve( edge, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'hermite' )
                matrix_mult( stack[-1], edge)
                draw_lines( edge, screen, color)
                
            elif command == 'sphere':
                polygon = []
                add_sphere( polygon, args[0], args[1], 0, args[2], 5 )
                matrix_mult( stack[-1], polygon)
                draw_polygons( polygon, screen, color)
                
            elif command == 'torus':
                polygon = []
                add_torus( polygon, args[0], args[1], 0, args[2], args[3], 5 )
                matrix_mult( stack[-1], polygon)
                draw_polygons( polygon, screen, color)
                
            elif command == 'box':
                polygon = []
                add_box( polygon, args[0], args[1], args[2], args[3], args[4], args[5] )
                matrix_mult( stack[-1], polygon)
                draw_polygons( polygon, screen, color)

            elif command == 'scale':
                s = make_scale( args[0], args[1], args[2] )
                matrix_mult( stack[-1], s)
                stack[-1] = s

            elif command == 'move':
                t = make_translate( args[0], args[1], args[2] )
                matrix_mult( stack[-1], t)
                stack[-1] = t

            elif command == 'rotate':
                angle = args[1] * ( math.pi / 180 )
                if args[0] == 'x':
                    r = make_rotX( angle )
                elif args[0] == 'y':
                    r = make_rotY( angle )
                elif args[0] == 'z':
                    r = make_rotZ( angle )
                matrix_mult( stack[-1] , r)
                stack[-1] = r

        elif command == 'push':
            stack.append(stack[-1])

        elif command == 'pop':
            stack.pop()
            
        elif command == 'ident':
            ident( stack[-1] )
            
        elif command == 'apply':
            matrix_mult( stack[-1], points )

        elif command == 'clear':
            points = []

        elif command in ['display', 'save' ]:
            #screen = new_screen()
            #draw_polygons( points, screen, color )
            
            if command == 'display':
                display( screen )

            elif command == 'save':
                c+= 1
                save_extension( screen, commands[c].strip() )
        elif command == 'quit':
            return
        c += 1
