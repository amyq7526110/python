#!/usr/bin/env python3
import os
import readline
a=os.popen('echo 1').readline()
print(a)
os.system('ls')

 #    循环概述
 #  •  一组被重复执行的语句称之为循环体,能否继续重复,
 #     决定循环的终止条件
 #  •  Python中的循环有while循环和for循环
 #  •  循环次数未知的情况下,建议采用while循环
 #  •  循环次数可以预知的情况下,建议采用for循环

 #  while循环语法结构
 #  •  当需要语句不断的重复执行时,可以使用while循环
 #  while  expression:	
 #     while_suite	

 #     语句while_suite会被连续不断的循环执行,直到表达
 #     式的值变成0或False

a=1

while a <= 20 :
   print(a,end=' ')
   a += 1
#
print()

a=1
 
while a <= 20:
   print(a,end=' ')
   a += 2


#  循环语句进阶

#   
#  break语句

#      break语句可以结束当前循环然后跳转到下条语句
#      写程序的时候,应尽量避免重复的代码,在这种情况
#      下可以使用while-break结构

name = input('username=')

while name !='tom':
   name = input('username=')

while  True:
   name = input('username=')
   if name == 'tom':
      break



#     continue语句

#     •  当遇到continue语句时,程序会终止当前循环,并忽
#     略剩余的语句,然后回到循环的顶端
#     •  如果仍然满足循环条件,循环体内语句继续执行,否
#     则退出循环

num=0

while num < 20:
   num += 1
   if num % 2 == 0:
      continue
   print(num,end=' ')
print()

#   else语句
#   •  python中的while语句也支持else子句
#   •  else子句只在循环完成后执行
#   •  break语句也会跳过else块

sum10 = 0 

i = 1

while i <= 10:
   sum10 += i
   i += 1
else:
   print(sum10)
   
#  死循环

#   条件永远满足的循环叫做死循环
#   使用break可以退出死循环
#   else永远不执行















