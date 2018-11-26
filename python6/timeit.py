#!/usr/bin/env python3
import time
import threading
def add(n):
    result = 0
    for i in range(1,n):
        result += i
    print(result) 

if __name__ == '__main__':
    start = time.time()
    tlist = []
    for i in range(2):
        t = threading.Thread(target=add,args=(50000001,))
        tlist.append(t)         # 将线程加入到列表
        t.start()
    for th in tlist:
        th.join()               # 在列表中取出线程，等待结束后向下执行
    end  = time.time()
    print(end - start )
