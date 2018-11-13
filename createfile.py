#!/usr/bin/env python3
import os
content = []
def test_file():
    "判断文件是否存在"
    filename =  input('please input a not exit filename: ')
    if  os.path.exists(filename):
        return 0 
    else: 
        return filename 
def get_content():
    "获取用户输入数据"  
    print('please input content and input "end" quit ')
    while True:
        filecont = input('> ')
        if filecont == 'end':
             break 
        content.append(filecont)
    return content
def wfile(filename,content):
    "将内容列表写入到文件"
    content = [ '%s\n' % line for line in content ]
    with open(filename,'w')  as wf:
        wf.writelines(content)     
if __name__ == '__main__':
    a = test_file()
    while not  a:
        a = test_file()
#    print(a)
    b =  get_content()
    wfile(a,b)  
    os.system("cat %s" % a )


