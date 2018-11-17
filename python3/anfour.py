#!/usr/bin/env python3
import  random
from math import sqrt
import  time
def set_time(func):
    def qiushi(): 
        a = time.time()
        b = func()
        c = time.time()
        return "%s 时间 %s " % (b  ,c - a)
    return qiushi
@set_time
def qiuPi():
    dimension=1000000
    maxshots=1000000
    def get_random():
        return random.randint(1,1000000)
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
    return Pi

print(qiuPi())

        
 



