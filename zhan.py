#!/usr/bin/env  python3
c=[]
def ruzhan(c):
    c.append(input('please input ruzhan content '))
def chuzhan(c):
    x  =   int(input('please input you want pop number'))
    if len(c) < x:
        print("don't have x de content")
    else:	
        for i in range(0,x):
            c.pop()
def chazhan(c):
    print(c)
def zhanmian():
    chioce  =  input('1 cha, 2 ru ,3 chu, other tuichu ')
    if chioce == '1':
        chazhan(c)
    elif chioce == '2':
        ruzhan(c)
    elif chioce == '3': 	
        chuzhan(c)
    elif   chioce == 'q':  
        exit(1)
if __name__ == '__main__':
    while True:
        zhanmian()
     
