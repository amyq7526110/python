#!/usr/bin/env python3
import threading 
import time
from apply import apply
nums = [4,2]
class ThreadFunc(object):   # 定义可调用类
    def __init__(self,func,args,name=''):
        self.name = name
        self.func = func 
        self.args = args
    def __call__(self):
        apply(self.func,self.args)
def loop(nloop,nsec): # 定义函数，打印运行的起止时间
    print('start loop %d  at %s ' % (nloop,time.ctime()))
    time.sleep(nsec)
    print('loop %d done at %s' % (nloop,time.ctime()))
def main():
    print('starting at : %s ' % time.ctime())
    threads = []
    for i in range(2):
        t = threading.Thread(target=ThreadFunc(loop,(i,nums[i]),loop.__name__))   
        threads.append(t)  # 创建两个线程，放入列表
    for i in range(2):
        threads[i].start()
    for i in range(2):
        threads[i].join()
    print('all Done at %s' % time.ctime())    
if __name__ == '__main__':
     main()

            

   

