#!/usr/bin/env python3


#  扩展if语句结构

#   if expression1:			
#      if_suite	
#   elif expression2:	
#      elif_suite	
#   .....
#   else:	
#      else_suite	

grade = int (input('请输入你的成绩：'))

if grade > 90:
   print('优秀')
elif grade > 80:
   print('好')
elif grade > 70:
   print('良')
elif  grade > 60:
   print('及格')
else:
   print('你没救了')


      
