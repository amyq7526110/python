#!/usr/bin/env python3 
import random
import re
all_choice=['剪刀','石头','布']
win = [['剪刀','布'],['石头','剪刀'],['布','石头']]
print('  0 = 剪刀,1 = 石头,2 = 布')
uwin=0
cwin=0
while uwin < 2 and cwin < 2  :
   cpnum = random.choice(all_choice)
   usnum = input('请输入你的选择: ')
   prog = re.compile(r'^[0-2]$')
   result = prog.match(usnum)
   if not  result:
      print('Usage: input 0-2')
      exit(0)
   usnum  = int(usnum)                
   usch = all_choice[usnum] 
   if [usch,cpnum] in win:
      uwin += 1
      print('你赢了','你是',usch,' 电脑是',cpnum)
      print('你赢了',uwin,'次',sep='')
   elif usch == cpnum:
      print('平局')
   else:
      cwin += 1
      print('你是',usch,' 电脑是',cpnum)
      print('电脑赢了',cwin,'次',sep='')
if uwin == 2:
   print('恭喜你')
else:
   print('倒霉吧')




    

 

