#!/usr/bin/env python3
import subprocess
import os
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
    for i in list:
        pid = os.fork()
        if not pid:
           scanhost(i)
           exit()
#    os.wait()
#    time.sleep(3)
#    print('\033[32mDone\033[0m')






