#!/usr/bin/env python3

import random
compunum = random.randint(1,100)

count=1

print('正确的数字：',compunum)
while count <= 5:

   usernum = int(input('请输入你猜的数字'))
   if usernum == compunum:
      print('你猜对了')
      exit(1)
   elif usernum <= compunum:
      print('你猜小了')
   else:
      print('你猜大了')
   count += 1
print('正确的数字：',compunum) 
    


 


 
