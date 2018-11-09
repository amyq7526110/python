#!/usr/bin/env python3

#  python 中的语句

#   顺序语句

#   判断语句

#   循环语句

      #  判断

      #  标准if条件语句的语法

      #   if 表达式:
      #      if_suite
      #   else 
      #      else_suite

      #   如果表达式的值非0或者为布尔值True, 则代码组
      #+  if_suite被执行;否则就去执行else_suite

      #   代码组是一个python术语,它由一条或多条语句组
      #+  成,表示一个子代码块

if 3>0:
   print('3 > 0 yes')
else:
   print('3 > 0 no')
        
     # •  只要表达式数字为非零值即为True      

if 10:
   print('yes')
else:
   print('no')

     #    空字符串、空列表、空元组,空字典的值均为False

if '':
   print('yes')
else:
   print('no')

user = 'mhw'
pwd = '123456'

a = input('username=')
b = input('password=')
if user == a: 
   if pwd == b:
      print('ok')
   else:
      print('password not ok')
else:
   print('username not ok')
x = 3
y = 4
smaller = x if x < y else y
print(smaller)

   


