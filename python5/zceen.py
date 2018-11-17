#!/usr/bin/env python3

import re
from collections import Counter

class CountPatt:
      def __init__(self,patt):
          self.cpatt = re.compile(patt)
      def count_patt(self,fname):
          result = Counter()
          with open(fname) as fobj:
               for line in fobj:
                   m = self.cpatt.search(line)
                   if m:
                        result.update([m.group()])
          return result

if __name__ == '__main__':
     fname = '/var/log/httpd/access_log'  
     ip = '^(\d{1,3}\.){3}\d{1,3}'
     cp = CountPatt(ip)
     access = cp.count_patt(fname)
     print(access)
     print(access.most_common(3))  # 访问最大的前三名
         
                      
            
                 
