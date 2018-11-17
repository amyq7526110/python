#!/usr/bin/env python3
from random  import randint
a = [ 4,2,5,3,9,1,8 ]
a = [ randint(1,10000) for i in range(1000) ]
# def zuobiao(a,left,right):
#      j = left
#      for i in range(left,right):
#          if a[i] < a[right] :
#             a[i],a[j]  = a[j],a[i] 
#             j += 1
#      a[j],a[right] = a[right],a[j]
#      return j

def zuobiao(a,left,right):
    i = left + 1
    j = right
#    x = right - left
#    print(i,j)
#    print('主元',a[left])
    while True:
        while a[i] < a[left] and i < right:
            i += 1
        while a[j] > a[left]  :
            j -= 1
#        print('i = ', i,'j=', j)
        if i >= j:
            break
#        print(a[i], a[j])
        a[j],a[i] = a[i],a[j]
#        print(a)
        i += 1
        j -= 1
    a[left],a[j] = a[j],a[left]
#    print('center',j)
    return j

def quicksort(a,left,right):
    if left  <  right:
        center =  zuobiao(a,left,right)
#        print(a)
        quicksort(a,left,center-1)
        quicksort(a,center+1 ,right)
print(a)
quicksort(a,0,len(a)-1)
print(a)

             
               
     


