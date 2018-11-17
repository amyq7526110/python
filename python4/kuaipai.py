#!/usr/bin/env python3

from random  import randint
#
# #def kpai(a):
# a = [ 4,2,5,3,7,1,8 ]
# # a= [randint(1,10) for i in range(9) ]
# i = 1
# j = len(a)-1
# print(a[0])
# print(a)
# while True:
#     while True:
#        if  a[0]  >=  a[i]:
#            i +=  1
#            break
#        else:
#            i = i + 1
#     while True:
#         if  a[0]  <=  a[j]:
#            j -= 1
#            break
#         else:
#            j -= 1
#     if i+1 >= j:
#         break
#     print(a[i],a[j])
#     a[i],a[j] = a[j],a[i]
#     print(a)
#
# a[0],a[i] =a[i],a[0]
# print(a)
#      return a
# a = [ randint(1,100) for i in range(10) ]
# print(a)
# print(kpai(a))
#
a = [ 9,2,5,3,7,1,4 ]
a = [ randint(1,100) for i in range(10) ]
def zuobiao(a,left,right):
     j = left
#     pri = a[right]
#     print(pri)
#     x = right - left
     for i in range(left,right):
         if a[i] < a[right] :
#            print(a)
            a[i],a[j]  = a[j],a[i] 
            j += 1
#            print(a)
  #       print()
     a[j],a[right] = a[right],a[j]
     return j

def quicksort(a,left,right):
    if left  <  right:
        center =  zuobiao(a,left,right)
 #       print(a,center)
        quicksort(a,left,center-1)
 #       print(a)
        quicksort(a,center+1,right)
 #       print(a)

quicksort(a,0,len(a)-1)
print(a)

             
               
     


