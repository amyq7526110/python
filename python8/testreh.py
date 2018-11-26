#!/usr/bin/env python3
from urllib import request

# html = request.urlopen('http://www.163.com/')
# print(html.readline())
# print(html.read(4096))
# print(html.readlines())
def get_file(url1,desr_fname):
    html = request.urlopen(url1)
    with open(desr_fname,'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    get_file('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E4%B8%89%E5%9B%BD%E5%BF%97','/tmp/zg.html')
