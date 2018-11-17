#!/usr/bin/env python3
import time

n = 0

while True:

    print('\r%s@%s' %  ('#' * n ,'#' * (19-n) ),end='')
    n += 1
    if n == 20:
       n = 0
    time.sleep(0.3) 


