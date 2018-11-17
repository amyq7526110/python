#!/usr/bin/env python3
from random import randint 
from functools import partial

#  偏函数
#  •  偏函数的概念是将函数式编程的概念和默认参数以及
#  可变参数结合在一起
#  •  一个带有多个参数的函数,如果其中某些参数基本上
#  固定的,那么就可以通过偏函数为这些参数赋默认值

def add(a,b,c,d,e):
    return a + b + c + d + e

print(add(10,20,30,40,50))           #  150
print(add(10,20,30,40,5))            #  105
print(add(10,20,30,40,150))          #  250

newadd = partial(add,10,20,30,40)

print(newadd(50))                    #  150
print(newadd(5))                     #  105
print(newadd(150))                   #  250


#  递归函数
#  •  如果函数包含了对其自身的调用,该函数就是递归的
#  •  在操作系统中,查看某一目录内所有文件、修改权限
#  等都是递归的应用

def func1(num):
    if num == 1: 
        return 1
    else:
        return num*func1(num-1)

print(func1(10))                  #  3628800 
print(func1(5))                   #  120 
x = [2,5]


#  案例3:快速排序
#  1.  随机生成10个数字
#  2.  利用递归,实现快速排序

nums = [ randint(1,100) for i in range(10) ]
print(nums)
def kuaipai(seq):
    if len(seq) < 2:
       return seq
    s = []
    l = []
    middle = seq[0]
    for i in seq[1:]:
        if i <= middle:
           s.append(i)
        else:
           l.append(i)
    return kuaipai(s) + [ middle ] + kuaipai(l)
print(kuaipai(nums))   
    
    
             
#   生成器
#   •  从句法上讲,生成器是一个带yield语句的函数
#   •  一个函数或者子程序只返回一次,但一个生成器能暂
#   停执行并返回一个中间的结果
#   •  yield 语句返回一个值给调用者并暂停执行
#   •  当生成器的next()方法被调用的时候,它会准确地从
#   离开地方继续    
        
    
#  生成器(续1)
#  •  与迭代器相似,生成器以另外的方式来运作
#  •  当到达一个真正的返回或者函数结束没有更多的值返
#  回,StopIteration异常就会被抛出

def mygen():
   a = 10 + 20
   yield a
   yield 'hello world'
   b = 'ni hao'
   yield b

mg = mygen()
print(mg.__next__())                  #   30
print(mg.__next__())                  #   hello world
print(mg.__next__())                  #   ni hao
#print(mg.__next__())                 #   StopIteration


newg = mygen()                        #   30
for item in newg:                     #   hello world
    print(item)                       #   ni hao





  















