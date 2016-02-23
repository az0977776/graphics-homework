from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    print "x0: " + str(x0)
    print "y0: " + str(y0)
    print "x1: " + str(x1)
    print "y1: " + str(y1)
    if (x0 > x1):
        dummy = x1
        x1 = x0
        x0 = dummy
    
    A = y1-y0
    B = -(x1-x0)
    if (B != 0):
        slope = A*1.0/(-1*B)
        print "slope: " +str(slope)
        
    #horizontal line
    if (A == 0):
        print "horizontal line"
        while (x0<=x1):
            plot(screen, color, x0, y0)
            x0+=1
            
    #vertical line
    elif (B == 0):
        print "vertical line"
        while (y0<=y1):
            plot(screen, color, x0, y0)
            y0+=1
            
    #octant2
    elif (slope > 1):
        print "octant 2"
        d = A + 2*B
        while(y0<=y1):
            plot(screen, color, x0, y0)
            if (d<0):
                x0+=1
                d+=2*A
            y0+=1
            d+=2*B
            
    #octant1
    elif (slope > 0):
        print "octant 1"
        d = 2*A + B
        while(x0<=x1):
            plot(screen, color, x0, y0)
            if (d>0):
                y0+=1
                d+=2*B
            x0+=1
            d+=2*A

    #octant8
    elif (slope > -1):
        print "octant 8"
        d = 2*A - B
        while (x0<=x1):
            plot(screen, color, x0, y0)
            if (d<0):
                y0-=1
                d-=2*B
            x0+=1
            d+=2*A
    
    #octant7
    else:
        print "octant 7"
        d = 2*B - A
        while (y0>=y1):
            plot(screen, color, x0, y0)
            if (d>0 ):
                x0-=1
                d-=2*A
            y0-=1
            d+=2*B
