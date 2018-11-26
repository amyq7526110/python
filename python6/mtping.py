#!/usr/bin/env python3
import subprocess
import threading

class Ping:
    def __init__(self,host):
        self.host = host
    def __call__(self):   
        rc = subprocess.call(
        'ping -c2 -i0.2 -W1 %s  &>/dev/null' % self.host,
        shell=True
        )
        if not rc:
            print('%s up' % self.host)
        else:
            print('%s down' % self.host)
if __name__ == '__main__':
    list =  [ '176.121.207.' + str(i) for i in range(1,255) ]
    for ip in list:
        t = threading.Thread(target=Ping(ip))
        t.start()

