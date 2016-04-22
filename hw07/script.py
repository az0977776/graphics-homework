import mdl
from display import *
from matrix import *
from draw import *

ARG_COMMANDS = [ 'line', 'scale', 'translate', 'xrotate', 'yrotate', 'zrotate', 'circle', 'bezier', 'hermite', 'sphere', 'box', 'torus']

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
    print p[0]
    
    c = 0
    if p:
        (commands, symbols) = p
        print commands
        print symbols
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    screen = new_screen()
        
    for command in commands:
        pass
        #print command
