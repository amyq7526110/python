#!/usr/bin/env python3
import os
import time


def zb(t):
    print('in child sleep %s ...'  % t)
    time.sleep(t)
    print('child %s done ' % t )
    exit()

pid = os.fork()
if not pid:
    zb(15)

pid = os.fork()
if not pid:
    zb(10)
time.sleep(20)    
print(os.waitpid(-1,1))                 # 一个waitpid只能处理一个僵尸进程
print(os.waitpid(-1,1))                 # 一个waitpid只能处理一个僵尸进程
time.sleep(10)
    
#  使用轮询解决zombie问题
#  •  父进程通过os.wait()来得到子进程是否终止的信息
#  •  在子进程终止和父进程调用wait()之间的这段时间,
#  子进程被称为zombie(僵尸)进程
#  •  如果子进程还没有终止,父进程先退出了,那么子进
#  程会持续工作。系统自动将子进程的父进程设置为
#  init进程,init将来负责清理僵尸进程使用轮询解决zombie问题(续1)
#  •  python可以使用waitpid()来处理子进程
#  •  waitpid()接受两个参数,第一个参数设置为-1,表示
#  与wait()函数相同;第二参数如果设置为0表示挂起父
#  进程,直到子程序退出,设置为1表示不挂起父进程
#  •  waitpid()的返回值:如果子进程尚未结束则返回0,
#  否则返回子进程的PID
