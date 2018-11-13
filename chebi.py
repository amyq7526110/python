#!/usr/bin/env python3
import re
import keyword
def chekey():
    test_str = input('please input a string: ')
    if test_str in keyword.kwlist:
        print('you input word in the keyword')
        exit(0)
    pattern = re.compile(r'^[^a-zA-Z_]')
    result =  pattern.match(test_str)
    if result:
        print('开头错了')
    a = re.split('\W',test_str)
#    print(a)
    c=[]
    j = 0
    for i in a:
        j += len(i) + 1 
        if j == 1:
            continue
        c.append('%d cuo le' % j )
    c.pop()
    for i in c:
        print(i)
    if len(a)  ==  1 :
        print(test_str,'is ok')
        exit(1)
if __name__ == '__main__':
    chekey()

    # pattern = re.compile(r'^[^a-zA-Z_]')
    # result =  pattern.findall(test_str)
    # print(result)
    # pattern2 = re.compile(r'[^a-zA-Z_]')
    # result2 = pattern2.findall(test_str)
    # print(result2)
