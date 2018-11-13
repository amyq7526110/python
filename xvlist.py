#!/usr/bin/env python3

#   序列

#   序列类型操作符

#   序列操作符      作用

#   seq[ind]        获得下标为ind的元素
#   seq[ind1:ind2]  获得下标从ind1到ind2间的元素集合
#   seq * expr      序列重复expr次
#   seq1 + seq2     连接序列seq1和seq2
#   obj in seq      判断obj元素是否包含在seq中
#   obj not in seq  判断obj元素是否不包含在seq中

#   内建函数

#   函 数           含 义

#   list(iter)      把可迭代对象转换为列表
#   str(obj)        把obj对象转换成字符串
#   tuple(iter)     把一个可迭代对象转换成一个元组对象

print(list('abc'))
print(list(range(10)))
print(list([1,2,3]))
# print(list(132))    #  报错

print(str(100))
print(str(True))

print(tuple(range(10)))
print(tuple('abc'))

#  内建函数(续1)

#   len(seq):返回seq的长度

#   max(iter,key=None):返回iter中的最大值

#   enumerate:接受一个可迭代对象作为参数,返回一
#   个enumerate对象

print(enumerate('abc'))

#  内建函数(续2)

#     reversed(seq):接受一个序列作为参数,返回一个以
#  逆序访问的迭代器

#     sorted(iter):接受一个可迭代对象作为参数,返回
#  一个有序的列表

print(reversed([1,2,3]))

for i in reversed([1,2,3]):
    print(i,end='')
print() 

print(sorted('abecd'))
print(sorted([1,4,3,7,6,8]))
print(sorted((1,10,8,5,9)))







