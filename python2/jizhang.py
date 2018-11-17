#!/usr/bin/env python3
import re
import pickle as p
import time
import os 
from  datetime  import datetime  
def chushi():
     a  =  [[time.time(),0,0,'wu',10000]]
     with open('jizhang.txt','wb') as wf:
          p.dump(a,wf)
def chaxun():
    with  open('jizhang.txt','rb') as wf:
       a = p.load(wf)
    for i in a:
        print('时间    ： %s' %  time.ctime(i[0]))
        print('这次开销： %d' % i[1])
        print('这次收入： %d' % i[2])
        print('说明    ： %s' % i[3]) 
        print('剩余钱数： %d\n' % i[4])                         
def jizhang():
   try:
      kx = int(input('开销 '))
      sr = int(input('收入 '))
      content =  input('说明 ')
      with open('jizhang.txt','rb') as wf:
           a = p.load(wf)
           zhonge = a[-1][-1] - kx + sr  
           a.append([time.time(),kx,sr,content,zhonge])  
      with open('jizhang.txt','wb') as wf:
           p.dump(a,wf)
   except (ValueError):
        print('请输入一个数字')
def jzmenu():
    record = 'jizhang.txt'
    if not os.path.exists(record):
         chushi()
    cmds = {'_1':chaxun,'_2':jizhang,'_3':chushi}
    patal = '''1 查帐
2 记账
3 初始化
q 退出
please input your chioce: '''  
    while True:
       choice = '_'+input(patal)
       if not  re.match(r'^_[123q]$',choice):
           continue
       if  choice == '_q':
           break
       cmds[choice]() 
if __name__ == '__main__':
    try:
        jzmenu()
    except (KeyboardInterrupt,EOFError):
        print('bye-bye')







