#!/usr/bin/env python3
import subprocess
import threading
import time

def scanhost(ip):
    rc = subprocess.call(
    'ping -c2 -i0.2 -W1 %s  &>/dev/null' % ip,
    shell=True
    )
    if not rc:
        print('%s up' % ip)
    else:
        print('%s down' % ip)

if __name__ == '__main__':
    list =  [ '176.121.207.' + str(i) for i in range(1,255) ]
    for ip in list:
        t = threading.Thread(target=scanhost,args=(ip,))
        t.start()


#   传递函数给Thread类
#   •  多线程编程有多种方法,传递函数给threading模块
#   的Thread类是介绍的第一种方法
#   •  Thread对象使用start()方法开始线程的执行,使用
#   join()方法挂起程序,直到线程结束




