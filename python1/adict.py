#!/usr/bin/env python3

#  基本数字类型

#  •  int:有符号整数
#  •  bool:布尔值
#  –  True:1
#  –  False:0
#  •  float:浮点数
#  •  complex:复数

# 数据类型比较
#•  按存储模型分类

#     标量类型:数值、字符串
#–    容器类型:列表、元组、字典

#•  按更新模型分类:

#–    可变类型:列表、字典
#–    不可变类型:数字、字符串、元组

#•  按访问模型分类

#–    直接访问:数字
#–    顺序访问:字符串、列表、元组
#–    映射访问:字典

args=('a',1)
print(args)
adict={'name':'bob','age':18}
print(adict['age'])
print(adict['name'])
adict['address']='bj'
print(adict)
adict['name']='lucy'
print(adict)
print('name' in adict)
print('bob' in adict)
print('address'  not in adict)
print('add' not in adict )

# 运算符号

# + - * / // %  

#  比较字符

#  数字比较

print('1>2',1>2)
print('2>1',2>1)
print('2==1',2==1)
print('2!=1',2!=1)

#  字符比较  根据首字母的‘ASCLL’的值比较

print('a > b','a'>'b')
print('admin > b','admin'>'b')


#  逻辑运算符


#  and or not 

print(' 1  and 1 ',1 and 1)
print(' 0  and 1 ',0 and 1)
print(' 1  and 0 ',1 and 0)
print(' 0  and 0 ',0 and 0)

print(' 1  or 1 ',1 or 1)
print(' 0  or 1 ',0 or 1)
print(' 1  or 0 ',1 or 0)
print(' 0  or 0 ',0 or 0)

print(' not  1 ',not 1)
print(' not  0 ',not 0)

#  判断合法用户
 
user = 'mhw'
pwd = '123456'
a = input('username=')
b = input('password=')
if user == a and pwd == b: 
   print('ok')
else:
   print('not ok')


   















