#!/usr/bin/env python3

# 字典基础操作

# 创建字典
  #  通过{ }操作符创建字典
  #  通过dict()工厂方法创建字典
  #  通过fromkeys()创建具有相同值的默认字典

adcit = {'name':'bob','age':23}

print(adcit)                #  {'name': 'bob', 'age': 23}
print(dict())               #  {}
print(dict(['ab']))         #  {'a': 'b'}
print(dict(['ab','cd']))    #  {'a': 'b', 'c': 'd'}
print(dict([('name','haha'),('age',16)]))  #{'name': 'haha', 'age': 16}
print({}.fromkeys(['bob','tmp','alse'],7)) #{'bob': 7, 'tmp': 7, 'alse': 7}

#  字典操作符
#  •  使用字典键查找操作符[ ],查找键所对应的值
#  •  使用in和not in判断键是否存在于字典中

print( 'bob' in adcit )     # False
print( 'name' in adcit )    # True
print(len(adcit))           # 2

#   访问字典
#   •  字典是映射类型,意味着它没有下标,访问字典中的
#   值需要使用相应的键

for key in adcit:                                # name :bob 
    print('%s :%s ' % (key,adcit[key]))          # age :23 
    
print('%(name)s: %(age)s' % adcit )              # bob: 23

#   更新字典
#   •  通过键更新字典
#   –  如果字典中有该键,则更新相关值
#   –  如果字典中没有该键,则向字典中添加新值

adcit = {'name':'bob','age':16,'email':'bbs@tedu.cn'}
adcit['age']  = 22


  

#   作用于字典的函数
#   •  len():返回字典中元素的数目
#   •  hash():本身不是为字典设计的,但是可以判断某个
#   对象是否可以作为字典的键
#   字典的key ,数字,字符串,元祖 不可变

hash(10)
hash('abc')


# 字典内建方法

print(adcit.get('name'))   #  对字典dict中的键
#                      key,返回它对应的值value,如果字典中不存在此键,
#                      则返回default的值


print(adcit.get('qq','123456'))
print(adcit.keys())                   # 返回keys
print(adcit.values())                 # 返回values
print(adcit.items())                  # 返回key values
adcit.update({'phone':'12312131'})
print(adcit)
adcit.pop('email')
print(adcit)

#   bob
#   123456
#   dict_keys(['name', 'age', 'email'])
#   dict_values(['bob', 22, 'bbs@tedu.cn'])
#   dict_items([('name', 'bob'), ('age', 22), ('email', 'bbs@tedu.cn')])
#   {'name': 'bob', 'age': 22, 'email': 'bbs@tedu.cn', 'phone': '12312131'}
#   {'name': 'bob', 'age': 22, 'phone': '12312131'}


#  字典内建方法(续2)
#  •  dict.setdefault(key, default=None):如果字典中
#  不存在key键,由dict[key]=default为它赋值
#  
#  字典内建方法(续3)

#  •  dict.items():返回一个包含字典中(键,值)对元组的列表
#  •  dict.keys():返回一个包含字典中键的列表
#  •  dict.values():返回一个包含字典中所有值的列表
#  •  dict.update(dict2):将字典dict2的键-值对添加到字典dict
#  •  dict.copy():返回字典(深复制)的一个副本







