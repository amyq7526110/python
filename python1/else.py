#!/usr/bin/env python3 



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
   
