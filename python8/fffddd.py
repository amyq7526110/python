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
        d = []
        cpatt = re.compile(r'(http|https)://[\w./-]+\.(jpg|png|gif|jpeg)')
        for line in fobj:
            print(line)
            m = re.search(cpatt,line)
            if m:
                d.append(m.group())
                print(m.group())
        return d
if __name__ == '__main__':
 #   get_file('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E4%B8%89%E5%9B%BD%E5%BF%97','/tmp/zg.html')
    x = guolv('/tmp/zg.html')
    print(len(x))
    for i in x:
        fname = '/tmp/haha/'+ os.path.basename(i)
        try:
            get_file(i,fname)
        except:
            continue