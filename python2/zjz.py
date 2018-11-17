#!/usr/bin/env python3

import pickle  as p
import time
import os 

def save(fname):
    amount = int(input("amount: ")) 
    comment = input("comment: ")
    with open(fname,'rb') as wf:
         a  = p.load(wf)
    balance = a[-1][-2] + amount
    a.append([time.time(),0,amount,balance,comment])
    with open(fname,'wb') as wf:
         p.dump(a,wf)
def cost(fname):
    amount = int(input("amount: ")) 
    comment = input("comment: ") 
    with open(fname,'rb') as wf:
         a  = p.load(wf)
    balance = a[-1][-2] - amount
    a.append([time.time(),amount,0,balance,comment])
    with open(fname,'wb') as wf:
         p.dump(a,wf) 
def view(fname):
    with  open(fname,'rb') as wf:
       a = p.load(wf)
    print(a) 
    for i in a:      
        print('时间    ： %s' %  time.ctime(i[0]))
        print('这次开销： %d' % i[1])
        print('这次收入： %d' % i[2])
        print('说明    ： %s' % i[4])
        print('剩余钱数： %d\n' % i[3])
def show_menu():
    fname = 'record.data'
    if not os.path.exists(fname): 
         init_data = [[ time.time(),0 ,0 ,10000,'开始记账']]
         with open(fname,'wb') as wf:
             p.dump(init_data,wf)    
    cmds = {'0':save,'1':cost,'2':view} 
    prompt = '''(0) save
(1) cost
(2) view
(q) quit
please input yout chioce(0/1/2/q)'''
    while True:  
        choice = input(prompt).strip()[0]
        if choice not in '012q':
            print('Invalid choice,Trt again')
            continue
        elif choice == 'q':
            break  
        cmds[choice](fname)
if __name__ == '__main__':
   show_menu()
  
