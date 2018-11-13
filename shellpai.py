#!/usr/bin/env  python3
from random import randint
def shell_sort(a):
    alist = a
    len_alist = len(alist)
    gap =  len_alist >> 1
    while gap >  1:
        gap = gap >> 1
        for i in range(gap,len_alist):
            temp = alist[i]
            end = i - gap
            while end >= 0 and alist[end] > temp:
    	         alist[end+gap]=alist[end]
    	         end = end - gap
            alist[end+gap]=temp
    print(alist)
if __name__ == '__main__':
     x = [ randint(1,100) for i in range(1,11) ]
     shell_sort(x)
    

   
