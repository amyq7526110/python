#!/usr/bin/env python3


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

  
