#!/usr/bin/python
import random

picture = "P3 500 500 255 "
for y in range(1,501):
    for x in range(1,501):
        r = 0
        g = (random.randint(1,100)+x)%256
        b = (random.randint(1,100)+y)%256
        picture += "%d %d %d "%(r,g,b) 

        
f = open("pic1.ppm", "w")
f.write(picture)
f.close()
