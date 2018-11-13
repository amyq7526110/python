#!/usr/bin/env python3

#  内建函数


#  •  string.capitalize():把字符串的第一个字符大写

mystr  =  'hello'

print(mystr.capitalize())  # Hello

print(mystr.title())       # Hello


#  •  string.center(width):返回一个原字符串居中,并
#  使用空格填充至长度width 的新字符串

print(mystr.center(50,'*'))  # 居中，在指定的宽度中剧中，和填充字符


#  •  string.count(str, beg=0,end=len(string)):返回str
#  在string里面出现的次数,如果beg或者end指定则
#  返回指定范围内str出现的次数

mystr = 'this is a test string'
print(mystr.count('is'))            # 2
print(mystr.count('is',4,100))      # 1



#   内建函数(续1)

#   •  string.endswith(obj, beg=0,end=len(string)):检
#   查字符串是否以obj结束,如果beg或者end指定则检
#   查指定的范围内是否以obj结束,如果是,返回True,
#   否则返回False

# endswith(str,start,end)

print(mystr.endswith('ing'))     # True       
print(mystr.endswith('ring'))    # True
print(mystr.endswith('string'))  # True
print(mystr.endswith('in'))      # False
print(mystr.endswith('is',0,4))  # True
  
#  所有字符变成大写

print(mystr.upper())    # THIS IS A TEST STRING
 

#  所有字符变成小写

print(mystr.lower())    # this is a test string

#   •  string.islower():如果string中包含至少一个区分大
#   小写的字符,并且所有这些字符都是小写,则返回
#   True,否则返回False

print(mystr.islower())  #  True


#   •  string.isupper():如果string中包含至少一个区分大
#   小写的字符,并且所有这些字符都是大写,则返回
#   True,否则返回False

print(mystr.isupper())  #  False


#   •  string.isdigit():如果string是否全是数字
#      则返回True,否则返回False

print(mystr.isdigit())    # False

mystr = '23456' 

print(mystr.isdigit())    # True


#   •  string.isalpha():如果string是否全是字母
#      则返回True,否则返回False

mystr = 'this string'

print(mystr.isalpha())     # False

mystr = 'thisstring'


print(mystr.isalpha())     # True


#  string.split(str="", num=string.count(str)):以str
#  为分隔符切片string,如果num有指定值,则仅分隔
#  num个子字符串

# 以str为准分割字符串，返回列表

mystr = 'this is a test string'

print(mystr.split(' ',))
print(mystr.split(' ',2))

#  去掉两端的空白字符

mystr = ' nihao  '

print(mystr.strip())










