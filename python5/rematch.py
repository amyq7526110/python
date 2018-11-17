#!/usr/bin/env python3
import re

#   match函数

#   •  尝试用正则表达式模式从字符串的开头匹配,如果匹
#   配成功,则返回一个匹配对象;否则返回None
#   >>> import re
#   >>> models = re.match('foo', 'food')           #成功匹配 
#   >>> print(m) 
#   <_sre.SRE_Match object; span=(0, 3), match='foo'> 
#   >>>  
#   >>> models= re.match(‘foo’, ‘seafood’)      #未能匹配 
#   >>> print(m) 
#   None

#  search函数
#  •  在字符串中查找正则表达式模式的第一次出现,如果
#  匹配成功,则返回一个匹配对象;否则返回None
#  >>> import re
#  >>> models= re.search('foo', 'food') 
#  >>> print(m) 
#  <_sre.SRE_Matchobject; span=(0, 3), match='foo'> 
#  >>>  
#  >>> models= re.search(‘foo’, ‘seafood’)      #可以匹配在字符中间的模式 
#  >>> print(m) 
#  <_sre.SRE_Matchobject; span=(3, 6), match='foo'> 

#  group方法
#  •  使用match或search匹配成功后,返回的匹配对象可
#  以通过group方法获得匹配内容
#  >>> import re
#  >>> models= re.match('foo', 'food') 
#  >>> print(m.group()) 
#  foo
#   
#  >>> models= re.search('foo', 'seafood') 
#  >>> m.group() 
#  'foo' 

#  findall函数
#  •  在字符串中查找正则表达式模式的所有(非重复)出
#  现;返回一个匹配对象的列表
#  >>> models= re.search('foo', 'seafoodisfood') 
#  >>> print(m.group())    #search只匹配模式的第一次出现 
#  foo
#  >>>  
#  >>> m = re.findall(‘foo’, ‘seafoodisfood’)  #获得全部的匹配项 
#  >>> print(m) 
#  ['foo', 'foo'] 


#  finditer函数
#  知
#  识
#  讲
#  解
#  •  和findall()函数有相同的功能,但返回的不是列表而
#  是迭代器;对于每个匹配,该迭代器返回一个匹配对
#  象
#  >>> m = re.finditer('foo', 'seafoodisfood') 
#  >>> for item in m: 
#          print(item.group()) 
#  ...




print(re.match('f..','food'))
print(re.match('f..','sedfood'))
m = re.search('f..','seafood is food')
print(m.group())
m = re.findall('f..','seafood is food')
print(m)
m = re.finditer('f..','seafood is food')
for m in  m:
    print(m.group())



#  split方法

#  •  根据正则表达式中的分隔符把字符分割为一个列表,
#  并返回成功匹配的列表

#  •  字符串也有类似的方法,但是正则表达式更加灵活
#  >>> importre   #使用.和-作为字符串的分隔符
#  
#  mylist= re.split('\.|-', 'hello-world.data') 
#  >>> print(mylist) 
#  ['hello', 'world', 'data'] 

mylist = re.split('\.|-','hello-world.data')
print(mylist)

#  sub方法

#  •  把字符串中所有匹配正则表达式的地方替换成新的字
#  符串
#  >>> m = re.sub('X', 'Mr.Smith', 'aVn: X\nDearX') 
#  >>> print(m) 
#  aVn: Mr.Smith
#  DearMr.Smith

#  compile函数
#  •  对正则表达式模式进行编译,返回一个正则表达式对
#  象
#  •  不是必须要用这种方式,但是在大量匹配的情况下,
#  可以提升效率
#  >>> paV= re.compile('foo') 
#  >>> models= paV.match('food') 
#  >>> print(m.group()) 
#  foo



#  贪婪匹配
#  •  *、+和?都是贪婪匹配操作符,在其后加上?可以取消
#  其贪婪匹配行为
#  •  正则表达式匹配对象通过groups函数获取子组


m = re.search('.+(\d+)', 'My phone number is : 14564654654')

print(m.group())        # My phone number is : 14564654654
print(m.group(1))       # 4

m = re.search('.+?(\d+)', 'My phone number is : 14564654654')

print(m.group())        # My phone number is : 14564654654  
print(m.group(1))       # 14564654654

















