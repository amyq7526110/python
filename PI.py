#!/usr/bin/env python3
import  random
from math import sqrt
dimension=10000000 
maxshots=10000000
def get_random():
    return random.randint(1,10000000)
shots = 0
splashes = 0
thuds = 0
Pi=0
while shots < maxshots:
    xCoord = get_random()
    yCoord = get_random()
    distance = sqrt(xCoord * xCoord + yCoord * yCoord)
    if distance < dimension:
         splashes += 1
    else:
         thuds += 1
    shots += 1
Pi = 4.000000000 * splashes / shots
print(Pi)

        
 



