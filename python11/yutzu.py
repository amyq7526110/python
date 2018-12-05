from  collections import namedtuple


# 命名元组
# •  命名元组与普通元组一样,有相同的表现特征,其添
# 加的功能就是可以根据名称引用元组中的项
# •  collections 模块提供了namedtuple()函数,用于创
# 建自定义的元组数据类型

poit = namedtuple('poit',['x','y','z'])
a = poit(10,20,30)
print(a.x)
print(a[1])
print(a[1:])
print(a.y)
print(a.z)