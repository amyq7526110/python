#!/usr/bin/env python3


import re 

class  LogAnalysis:
    def __init__(self,logfile,postion):
        self.logfile = logfile
        self.postion = postion
    
    def fenxi(self):
        b = {}
        with open(self.logfile)  as wf:
            while 1:
               data = wf.readline()
               if  not data:
                   break
               patt = re.compile(self.postion)
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
    a = LogAnalysis(logfile,'(\d{1,3}\.){3}\d{1,3}')
    b = LogAnalysis(logfile,'Chrome|curl|Firefox')
    print(a.fenxi())
    print(b.fenxi())
      
