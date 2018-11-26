#!/usr/bin/env python3

import threading
import time
nums = [4,2]

def loop(nloop,nsec): #  定义函数,打印运行的起止时间
    print('start loop %d,at %s ' % (nloop,time.ctime()))
    time.sleep(nsec)
    print('loop %d done at %s' % (nloop,time.ctime()))
def main():
    print('starting at : %s' % time.ctime())
    threadsd = []
    for i in range(2):
        t = threading.Thread(target = loop,args=(i,nums[i]))
        threadsd.append(t) 
    for i in range(2):
        threadsd[i].start()  # 同时运行两个线程
    for i in range(2):
        threadsd[i].join()   # 主程序挂起，直到所有线程结束
    print('all Done at %s' % time.ctime())
if __name__ == '__main__':
    main()


    
    
