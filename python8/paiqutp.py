#!/usr/bin/env python3
from urllib import request
import re
import os
# html = request.urlopen('http://www.163.com/')
# print(html.readline())
# print(html.read(4096))
# print(html.readlines())
def get_file(url1,dest_fname):
    html = request.urlopen(url1)
    with open(dest_fname,'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)
    return dest_fname        
            
def guolv(dest_fname,charset='utf8'):
    with open(dest_fname,'r',encoding=charset) as fobj:
        data = ''
        for line in fobj:
            data += line
        x = re.split('"',data)
        y = re.compile(r'(http|https)://[\w./-]+\.(jpg|png|gif|jpeg)')
        d = []
        for i in x:
            u = re.search(y,i)
            if u:
                d.append(u.group())
        return d
if __name__ == '__main__':
    get_file('https://www.163.com/','/tmp/163.html')
    x = guolv('/tmp/zg.html')
    print(x)
    for i in x:
        fname = '/tmp/haha/'+ os.path.basename(i)
        try:
            get_file(i,fname)
        except:
            continue


