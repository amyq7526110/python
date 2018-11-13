#!/usr/bin/env python3

  
#      创建及访问列表
#      •  列表是有序、可变的数据类型
#      •  列表中可以包含不同类型的对象
#      •  列表可以由[]或工厂函数创建
#      •  支持下标及切片操作


#   更新列表
#   •  通过下标只能更新值,不能使用标添加新值
#   >>> alist= [10, 35, 20, 80] 
#   >>> alist[-1] = 100
#   >>> alist[1:3] = [30, 50, 80] 


#   列表内建函数
#   列表方法                 操作

#   list.append(obj)         向列表中添加一个对象obj
#   list.count(obj)          返回一个对象obj 在列表中出现的次数
#   list.extend(seq)         把序列seq的内容添加到列表中
#   list.index(obj)          返回obj对象的下标
#   list.insert(index, obj)  在索引量为index 的位置插入对象obj
#   list.reverse()           原地翻转列表
#   list.sort()              排序

alist = [1,2,3]

#  向列表中添加一个对象obj

# alist.append(4)

# alist.append([5,6])    # [1, 2, 3, 4, [5, 6]]

# 追加一个元素

#  print(alist)

#  把序列seq的内容添加到列表中

#  alist.extend([4,5,6])   #  [1, 2, 3, 4, 5, 6]

#  print(alist)


#  list.insert(index, obj)  在索引量为index 的位置插入对象obj

#  alist.insert(0,0)

#  print(alist)   #  [0, 1, 2, 3]

#  插入内容后，原元素的位置向后移

#  alist.insert(-1,4)

#  print(alist)  # [1, 2, 4, 3]


#   list.reverse()           原地翻转列表
#   list.sort()              排序

alist = [1,1,2,5,98,4]

#  alist.sort() 
#  
#  print(alist)  # [1, 1, 2, 4, 5, 98]
#  
#  alist.reverse()
#  
#  print(alist)  # [98, 5, 4, 2, 1, 1]


#   list.index(obj)          返回obj对象的下标


# print(alist.index(98))      #  4

# print(alist.index(10))      # ValueError: 10 is not in list


#   list.pop()      取出栈顶的值 

print(alist.pop()) 
print(alist)
print(alist.pop()) 
print(alist)











