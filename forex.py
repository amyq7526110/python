#!/usr/bin/env python3
import re


#   for循环语法结构
#   •  python中的for接受可迭代对象(例如序列或迭代器)
#   作为其参数,每次迭代其中一个元素

#   fori iter_var in iterable:	
#   	suite_to_repeat
#   •  与while循环一样,支持break、continue、else语句
#   •  一般情况下,循环次数未知采用while循环,循环次
#   数已知,采用for循环

#   range函数
#   •  for循环常与range函数一起使用
#   •  range函数提供循环条件
#   •  range函数的完整语法为:
#   range(start, end, step =1)

for i in range(1,11):
    print(i,end=' ')
print()
for i in range(1,21,2):
    print(i,end=' ')

print()

#  案例1:斐波那契数列
sum=[0,1 ]
x = int(input('请输入一个数字'))

for i in range(0,x):    
    if i == 0:
       print(sum[i],end=' ')
    elif i == 1:
       print(sum[i],end=' ')
    else:
       sum.append(sum[-1]+sum[-2])
       print(sum[i],end=' ')  
print()


#  生成1-20 加入到列表中

alist = []

for i in range(1,21):
    alist.append(i)
print(alist) 

a=[ i  for i in range(1,21) ]
print(a)
for i in a: 
    print(i,end=' ')
print()
b={'a':'b','c':'d'}
for i in b:
    print(i,b[i])
c=[   i for i in range(1,21) if 1 % 2 == 1  ]
print(c)






   
