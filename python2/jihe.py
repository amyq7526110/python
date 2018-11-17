#!/usr/bin/env python3

# 集合

#   •  数学上,把set称做由不同的元素组成的集合,
#      集合(set)的成员通常被称做集合元素

#   •  集合对象是一组无序排列的可哈希的值

#   •  集合有两种类型


#   –  可变集合set


#   –  不可变集合frozenset

#   集合类型操作符
#   •  集合支持用in和not in操作符检查成员
#   •  能够通过len()检查集合大小
#   •  能够使用for迭代集合成员
#   •  不能取切片,没有键


a = set('abc')
b = set('bcd')
print(a)
print(b)

#  {'b', 'a', 'c'}
#  {'b', 'd', 'c'}

#  像一个无值的字典

c = set(['abc','hello',123])
print(c)
#  {123, 'hello', 'abc'}

for item in c:
   print(item)

#  123
#  hello
#  abc

print(a & b)   # {'b', 'c'}
print(a | b)   # {'a', 'b', 'd', 'c'}
print(a - b)   # {'a'}
 
#    集合内建方法
#    •  set.add():添加成员
#    •  set.update():批量添加成员
#    •  set.remove():移除成员


c.add('haha')
print(c)                  # {123, 'haha', 'abc', 'hello'}
c.update(['ni','hao'])    # {'haha', 'abc', 'ni', 'hao', 123, 'hello'}
print(c)


#   集合内建方法(续1)
#   •  s.issubset(t):如果s是t的子集,则返回True,否则返回False
#   •  s.issuperset(t):如果t是s的超集,则返回True,否则返回False
#   •  s.union(t):返回一个新集合,该集合是s和t的并集
#   •  s.intersection(t):返回一个新集合,该集合是s和t的交集
#   •  s.difference(t):返回一个新集合,该集合是s的成员,但不是t的成员

print(a.issubset(b))         #  False                
print(a.issuperset(b))       #  False
print(a.union(b))            #  {'a', 'd', 'b', 'c'}
print(a.intersection(b))     #  {'b', 'c'}
print(a.difference(b))       #  {'a'}









 
