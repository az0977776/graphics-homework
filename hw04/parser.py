from display import *
from matrix import *
from draw import *

ARG_COMMANDS = [ 'line', 'scale', 'translate', 'xrotate', 'yrotate', 'zrotate', 'circle', 'bezier', 'hermite', 'box', 'sphere', 'torus']

def parse_file( f, points, transform, screen, color ):

    commands = f.readlines()

    c = 0
    while c  <  len(commands):
        cmd = commands[c].strip()

        if cmd[0] == '#':
            c += 1
        
        elif cmd in ARG_COMMANDS:
            c+= 1
            args = commands[c].strip().split(' ')
            i = 0
            while i < len( args ):
                args[i] = float( args[i] )
                i+= 1

            if cmd == 'line':
                    add_edge( points, args[0], args[1], args[2], args[3], args[4], args[5] )
                    
            elif cmd == 'box':
                add_box( points, args[0], args[1], args[2], args[3], args[4], args[5] )
            elif cmd == 'circle':
                add_circle( points, args[0], args[1], 0, args[2], .01 )
                
            elif cmd == 'bezier':
                add_curve( points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'bezier' )
                
            elif cmd == 'hermite':
                add_curve( points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'hermite' )
                
            elif cmd == 'scale':
                s = make_scale( args[0], args[1], args[2] )
                matrix_mult( s, transform )
                
            elif cmd == 'translate':
                t = make_translate( args[0], args[1], args[2] )
                matrix_mult( t, transform )
                
            #angle = args[0] * ( math.pi / 180 )
            elif cmd == 'xrotate':
                r = make_rotX( args[0] )
                matrix_mult( r, transform )
            elif cmd == 'yrotate':
                r = make_rotY( args[0] )
                matrix_mult( r, transform )
            elif cmd == 'zrotate':
                r = make_rotZ( args[0] )
                matrix_mult( r, transform )
                
            elif cmd == 'box':
                add_box(points, args[0], args[1], args[2], args[3], args[4], args[5])
            elif cmd == 'sphere':
                add_sphere(points, args[0], args[1], args[2], args[3], 0.01)
            elif cmd == 'torus':
                add_torus(points, args[0], args[1], args[2], args[3], args[4], 0.01)
        else:
            if cmd == 'ident':
                ident( transform )
                
            elif cmd == 'apply':
                matrix_mult( transform, points )
                    
            elif cmd == 'print':
                print_matrix(points)
            
            elif cmd in ['display', 'save' ]:
                screen = new_screen()
                draw_lines( points, screen, color )
            
            elif cmd == 'display':
                display( screen )

            elif cmd == 'save':
                c+= 1
                save_extension( screen, commands[c].strip() )
            elif cmd == 'quit':
                return    
            elif cmd == 'clear':
                points = []
            else:
                print 'Invalid command: ' + cmd
        c+= 1
