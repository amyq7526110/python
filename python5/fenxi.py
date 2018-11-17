#!/usr/bin/env python3


import re

# a = '176.121.207.186 - - [07/Nov/2018:11:51:10 +0800] "GET / HTTP/1.1" 403 4897 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"'

def fenxi(logfile,postion):
    b = {}
    with open(logfile)  as wf:
        while 1:
           data = wf.readline()      
           if  not data:
               break
           patt = re.compile(postion)
           cpatt = patt.search(data)
           try:
               x = cpatt.group()
           except  (NameError,AttributeError):
               continue  
           if x not in b:
               b[x] = 1
           else: 
               b[x] += 1
    return b

if __name__ == '__main__':
   logfile = '/var/log/httpd/access_log'
   print(fenxi(logfile,'(\d{1,3}\.){3}\d{1,3}'))
#   print(fenxi(logfile,'Firefox'))
#   print(fenxi(logfile,'curl'))
   print(fenxi(logfile,'Chrome|curl|Firefox'))
