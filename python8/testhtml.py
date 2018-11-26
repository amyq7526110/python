#!/usr/bin/env python3
import re

def guolv(dest_fname):
    with open(dest_fname,'r') as fobj:
        data = ''
        for line in fobj:
           data += line
     #   print(data)

        x = re.split('"',data)
        y = re.compile(r'http.*.jpg$')
        d = []
        for i in x:
            u = re.search(y,i)
            if u:
                d.append(u.group())
        print(d)
if __name__ == '__main__':
    guolv('/tmp/zg.html')
            

