#!/usr/bin/env python3

#  
#  1.  一行代码实现1--100之和
#      利用sum()函数求和

print(sum(range(101)))

#  2.  如何在一个函数内部修改全局变量
#      利用global 修改全局变量

a = 5

def fn():
    global a
    a = 4 
fn()
print(a)

#  3.  列出5个python标准库

#  os：提供了不少与操作系统相关联的函数
#  sys:   通常用于命令行参数
#  re:   正则匹配
#  math: 数学运算
#  datetime:处理日期时间
#  urllib

#  4.  字典如何删除键和合并两个字典

#      del和update方法

dic = {'name':'bob','age':16}
del dic['name']
print(dic)
dic2 = {'name':'bob'}
dic.update(dic2)
print(dic)

#  5.  谈下python的GIL

#       GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，
#       一个线程在运行python程序的时候会霸占python解释器（加了一
#       把锁即GIL），使该进程内的其他线程无法运行，等该线程运行完
#       后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释
#       器锁解开，使其他线程运行。所以在多线程中，线程的运行仍是有
#       先后顺序的，并不是同时进行。多进程中因为每个进程都能被系统
#       分配资源，相当于每个进程有了一个python解释器，所以多进程可
#       以实现多个进程的同时运行，缺点是进程系统资源开销大


#  6.  python实现列表去重的方法

#      先通过集合去重，在转列表

lis = [ 12 ,11,11,22,33,45,11,12 ]
a = set(lis)
print(a)
x = []
[x.append(i) for i in a ]
print(x)

#  7.  fun(*args,**kwargs)中的*args,**kwargs什么意思？

#      *argv 和 **kward 主要用于函数定义。你可以将不定数量的参数
#       传递给一个函数。这里的不定的意思是预先不知道，函数使用者会
#       传递多少个参数给你，所以在这个场景下使用这两个关键字

#        *args 是用来发送一个非键值对的可变参数列表给一个函数

def demo(args_f,ass,*argv_v):
    print(args_f+'haha') 
    for x in argv_v:
        print(x)
demo('a','b','c','d')        

#        **kwargs 允许你将不定长度的键值对，作为参数传递个一个
#        函数，如果你想要在一个函数里处理带名字的参数，你应该
#        使用**kwargs

def dome(**arg_v):
    print(arg_v)
    for k,y in arg_v.items():
        print(k,y)
dome(jie='acd',age=16)    
 
#      
#  8.  python2和python3的range（100）的区别

#      python2返回列表，python3返回迭代器，节约内存



#  9.  一句话解释什么样的语言能够用装饰器?

#      函数可以作为参数传递的语言，可以使用装饰器


#  10.  python内建数据类型有哪些

#       整型--int
#       布尔型--bool
#       字符串--str
#       列表--list
#       元组--tuple
#       字典--dict

#  11.  简述面向对象中__new__和__init__区别

#       __init__是初始化方法，创建对象后，就立刻被默认调用了，可接收参数，如图

class Dike:

    def __init__(self,newnum,newcolor):
        self.newnum = newnum
        self.newcolor = newcolor
    def move(self):
        print('车会跑')
# 创建对象
BM = Dike(2,'red')
print('车的颜色为 %s' % BM.newcolor)
print('车的轮子数 %s' % BM.newnum)


#  1.   __new__至少要有一个参数cls，代表当前类，此参数在
#       实例化时由Python解释器自动识别

#  2.   __new__必须要有返回值，返回实例化出来的实例，
#       这点在自己实现__new__时要特别注意，可以return父类
#      （通过super(当前类名, cls)）__new__出来的实例，或者直接
#       是object的__new__出来的实例

#  3.  __init__有一个参数self，就是这个__new__返回的实例，
#      __init__在__new__的基础上可以完成一些其它初始化的动作，
#      __init__不需要返回值

#  4.  如果__new__创建的是当前类的实例，会自动调用__init__函数，
#      通过return语句里面调用的__new__函数的第一个参数是cls来保
#      证是当前类实例，如果是其他类的类名，；那么实际创建返回的
#      就是其他类的实例，其实就不会调用当前类的__init__函数，
#      也不会调用其他类的__init__函数。

class A(object):
    def __init__(self):
        print('这是 init 方法',self)

    def __new__(cls):
        print('这是cls 的 id',id(cls))
        print('这是new 方法',object.__new__(cls))
        return object.__new__(cls)
A()
print('这是类A的id',id(A))


#  12.  简述with方法打开处理文件帮我我们做了什么？

#       打开文件在进行读写的时候可能会出现一些异常状况，
#       如果按照常规的f.open写法，我们需要try,except,finally，
#       做异常判断，并且文件最终不管遇到什么情况，都要执行
#       finally f.close()关闭文件，with方法帮我们实现了finally
#       中f.close（当然还有其他自定义功能，有兴趣可以研究with方法源码）

f=open('list.sh','r')
try:
    data = f.read()
except:
    pass
else:
    print(data.strip())
finally:
    f.close()

#  13.  列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
#      map（）函数第一个参数是fun，第二个参数是一般是list，第三个参数可以写list，也可以不写，根据需求

list1 = [ 1, 2, 3, 4, 5 ]
res = map(lambda x : x**2  , list1)
res = [ i for i in res if i > 10  ]
print(res)

#  14.  python中生成随机整数、随机小数、0--1之间小数方法

#       随机整数：random.randint(a,b),生成区间内的整数

#       随机小数：习惯用numpy库，利用np.random.randn(5)生成5个
#                 随机小数
#       0-1随机小数：random.random(),括号中不传参

import random
import numpy 

result = random.randint(10,20)
res = numpy.random.randn(5)
ret = random.random()  #  不能传参数
print('\n正整数 %s \n\n5个随机小数 %s \n\n0-1随机小数 %s' % (result,res,ret))



#  15.  避免转义给字符串加哪个字母表示原始字符串？

#       r , 表示需要原始字符串，不转义特殊字符



#  16.  <div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
import re

trs = '<div class="nam">中国</div>'
res = re.search(r'<div class=".*">(.*)</div>',trs)
ret = re.findall(r'<div class=".*">(.*?)</div>',trs)
print(res.group(1))
print(ret)


#  17.  python中断言方法
#       举例assert（）方法，断言成功，则程序继续执行，断言失败，则程序报错

a = 3 
assert(a>1)
print('断言成功，继续执行')

b=4
# assert(b>7
print('断言失败，程序报错')

#  18.  数据表student有id,name,score,city字段，其中name中的名字可有重复，
#       需要消除重复行,请写sql语句

#       select  distinct  name  from  student

#  19.  10个Linux常用命令

#      ls  pwd  cd  touch  rm  mkdir  tree  cp  mv  cat  more  grep  echo 


#  20.  python2和python3区别？列举5个

#  1.  Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比如 print 'hi'
#  2.  python2 range(1,10)返回列表，python3中返回迭代器，节约内存
#  3.  python2中使用ascii编码，python中使用utf-8编码
#  4.  python2中unicode表示字符串序列，str表示字节序列      python3中str表示字符串序列，byte表示字节序列
#  5.  python2中为正常显示中文，引入coding声明，python3中不需要
#  6.  python2中是raw_input()函数，python3中是input()函数


#  21.  列出python中可变数据类型和不可变数据类型，并简述原理

#       不可变数据类型：数值型、字符串型string和元组tuple

#       不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，在内存中则只有一个对象（一个地址），如下图用id()方法可以打印对象的id
a = 3
b = 3
print(id(a))
print(id(b))
c = 'name'
d = 'name'
print(id(c))
print(id(d))
#       可变数据类型：列表list和字典dict；允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，不过对于相同的值的不同对象，在内存中则会存在不同的对象，即每个对象都有自己的地址，相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实在在的对象
a = [ 1,2 ]
b = [ 1,2 ]
print(id(a))
print(id(b))

#  22.  s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"

#       set去重，去重转成list,利用sort方法排序，reeverse=False
#       是从小到大排list是不 变数据类型，s.sort时候没有返回值，
#       所以注释的代码写法不正确

s = "ajldjlajfdljfddd"
s = set(s)
s = list(s)
# s = s.sort(reverse=False)
s.sort(reverse=False)
res =  "".join(s)
print(res)



#  23.  用lambda函数实现两个数相乘

sum = lambda x,y : x * y
print(sum(3,4))

#  24.  字典根据键从小到大排序dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}

dict1 = {"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
print(dict1.items())
list1 = sorted(dict1.items(),key = lambda i:i[0],reverse=False)
print('sorted 根据字典的建排序',list1)
new_dict = {}
for i in list1:
    new_dict[i[0]] = i[1]
print('新字典',new_dict)

#  25.  利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h" 
from collections import Counter 

a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res = Counter(a)
print(res)

#  26.  字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"顺便贴上匹配小数的代码，虽然能匹配，但是健壮性有待进一步确认

a = "not 404 found 张三 99 深圳"
res = re.sub('[0-9a-zA-Z]+','',a)
list1 = a.split(' ')
print(list1)
print(res.strip())
ret = re.findall(r'\d+|[a-zA-Z]+',a)
for i in ret:
    if i in list1:
        list1.remove(i)
new_str=' '.join(list1)        
print(ret)
print(new_str)

#  27.  filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#        filter() 函数用于过滤序列，过滤掉不符合条件的元素，
#        返回由符合条件元素组成的新列表。该接收两个参数，第一
#        个为函数，第二个为序列，序列的每个元素作为参数传递给
#        函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表

a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = filter(lambda x : x % 2 == 1 ,a)
print(list(res))




#  28.  列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



res = [ i for i in a if i % 2  == 1 ]
print(res)

#  29.  正则re.complie作用

#    re.compile是将正则表达式编译成一个对象，加快速度，并重复使用


#  30.  a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
print(type((1,)))   #   <class 'tuple'>
print(type((1)))    #   <class 'int'>
print(type(("1")))  #   <class 'str'>


#  31.  两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]

#     extend可以将另一个集合中的元素逐一添加到列表中，区别于append整体添加

list1 = [ 1,5 , 7 , 9  ]
list2 = [ 2 , 2, 6 , 8 ]
list1.extend(list2)
list1.sort(reverse=False)
print(list1)


#  32.  用python删除文件和用linux命令删除文件方法

#      python：os.remove(文件名)
#      linux:  rm 文件名


#  33.  log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”顺便把星期的代码也贴上了

import datetime
weeis = {'1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'天'}
s = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '  星期' + weeis[str(datetime.datetime.now().isoweekday())]
print(s)


#  34.  数据库优化查询方法
#   外键、索引、联合查询、选择特定字段等等 

#  35.  请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行

#   pychart、matplotlib


#  36.  写一段自定义异常代码自定义异常用raise抛出异常

def fun():
   try:

     for i in range(5):
         if i > 2:
             raise Exception('数字大于二了')
   except Exception as res:
        print(res)
fun()            

#  37.  正则表达式匹配中，（.*）和（.*?）匹配区别？

#       （.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配
#       （.*?）是非贪婪匹配，会把满足正则的尽可能少匹配

s = 'abcdabcda'
print('字符串',s)
res1=re.findall(r'a(.*)a',s)
print('贪婪匹配',res1)
res2=re.findall(r'a(.*?)a',s)
print('非贪婪匹配',res2)


#  38.  简述Django的ormORM

#       全拼Object-Relation Mapping，意为对象-关系映射实现了数据模
#       型与数据库的解耦，通过简单的配置就可以轻松更换数据库，而不
#       需要修改代码只需要面向对象编程,orm操作本质上会根据对接的数
#       据库引擎，翻译成对应的sql语句,所有使用Django开发的项目无需
#       关心程序底层使用的是MySQL、Oracle、sqlite....，如果数据库迁
#       移，只需要更换Django的数据库引擎即可


#     modies.py          Djiango          ORM                    关系型数据库

#    定义模型类，通过                   在ORM中，根据模型类       
#    属性体现对象间的                   生成与表的对应关系        SQLite
#    关系

#    调用模型对象的save()  <--------->  生成insert,updata语句
#                                                                  Mysql
#    调用模型类对象的Delete()  <----->  生成delete 语句    
#                                                                  Oracle
#    调用模型类的 all() get()  <----->  生成select语句   






#  39.  [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
#       列表推导式的骚操作运行过程：for i in a ,每个i是【1,2】，【3,4】，【5,6】，for j in i，每个j就是1,2,3,4,5,6,合并后就是结果
#       还有更骚的方法，将列表转成numpy矩阵，通过numpy的flatten（）方法，代码永远是只有更骚，没有最骚

a  =  [[1,2],[3,4],[5,6]]         
p = [ j  for i in a for j in i  ]
print(p)
import numpy as np
o  =  np.array(a).reshape(1,6).flatten().tolist()
print(o)
u = np.array(a)
c = u.reshape(1,6)
print(c)
for i in c:
    print(list(i))
    for j in i:
        print(j)

#  40.  x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果

#       join()括号里面的是可迭代对象，x插入可迭代对象中间，
#       形成字符串，结果一致，有没有突然感觉字符串的常见操 
#       作都不会玩了顺便建议大家学下os.path.join()方法，拼
#       接路径经常用到，也用到了join,和字符串操作中的join有
#       什么区别，该问题大家可以查阅相关文档，后期会有答案

x="abc"
y="def"
z=["d","e","f"]

m = x.join(y)
n = x.join(z)
o = y.join(x)
print(o)
print(m)
print(n)


#  41.  举例说明异常模块中try except else finally的相关意义

#       try..except..else没有捕获到异常，执行else语句
#       try..except..finally不管是否捕获到异常，都执行finally语句

try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产生了错误 %s ' % errorMsg)
else:
    print('没有捕获到异常，则执行该条语句')

try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产生了错误 %s ' % errorMsg)
finally:
    print('不管是否捕获到异常，都执行该条语句')


#  42.  python中交换两个数值

a, b = 3, 4
print(a,b)
a, b = b, a
print(a,b)

#  43.  举例说明zip（）函数用法

#     zip()函数在运算时，会以一个或多个序列（可迭代对象）做为参数，
#     返回一个元组的列表。同时将这些序列中并排的元素配对。zip()参数
#     可以接受任何类型的序列，同时也可以有两个以上的参数;当传入参数
#     的长度不同时，zip能自动以最短序列长度为准进行截取，获得元组。


a = [1,2]
b = [3,4]

res = [ i for  i in zip(a,b) ]
print(res)

a = (1,2)
b = (3,4)
res = list(zip(a,b))
print(res)

a = "ab"
b = "xyz"

res = [ i for i  in  zip(a,b) ]
print(res)


#  44.  a="张明 98分"，用re.sub，将98替换为100

a = "张明 98分"
res = re.sub('\d+','100',a)
print(res)

#  45.  写5条常用sql语句

#       show databases;
#       show tables;
#       desc 表名;
#       select * from 表名;
#       delete from 表名 where id=5;
#       update students set gender=0,hometown="北京" where id=5

#  46.  a="hello"和b="你好"编码成bytes类型

a = b'hello'
b = '哈哈'.encode()
print(a,b)
print(type(a),type(b))



#  47.  [1,2,3]+[4,5,6]的结果是多少？


#      两个列表相加，等价于extend

a = [ 1,2,3 ]
b = [ 4,5,6 ]
res = a + b
print(res)

#  48.  提高python运行效率的方法

#  1.  使用生成器，因为可以节约大量内存
#  2.  循环代码优化，避免过多重复代码的执行
#  3.  核心模块用Cython  PyPy等，提高效率
#  4.  多进程、多线程、协程
#  5.  多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率



#  49.  简述mysql和redis区别

#       redis： 内存型非关系数据库，数据保存在内存中，速度快
#       mysql： 关系型数据库，数据保存在磁盘中，检索的话，
#               会有一定的Io操作，访问速度相对慢

#  50.  遇到bug如何处理

#  1.  细节上的错误，通过print（）打印，能执行到print（）
#      说明一般上面的代码没有问题，分段检测程序是否有问题，
#      如果是js的话可以alert或console.log


#  2.  如果涉及一些第三方框架，会去查官方文档或者一些技术博客。


#  3.  对于bug的管理与归类总结，一般测试将测试出的bug用teambin等
#      bug管理工具进行记录，然后我们会一条一条进行修改，修改的过
#      程也是理解业务逻辑和提高自己编程逻辑缜密性的方法，我也都
#      会收藏做一些笔记记录。

#  4.  导包问题、城市定位多音字造成的显示错误问题



#  51.  正则匹配，匹配日期2018-03-20

url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-21&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
#       仍有同学问正则，其实匹配并不难，提取一段特征语句，用（.*?）匹配即可

patt = re.compile(r'(\d{4}-\d{2}-\d2)')
res = patt.findall(url)
res2 = re.findall(r'dateRange=(.*?)%7c(.*?)&',url)
print(res2)
print(res)



#  52.  list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]

#       利用min()方法求出最小值，原列表删除最小值，新列表加入最小值，
#       递归调用获取最小值的函数，反复操作

from random import choice 
list1 = [2,3,5,4,9,6]
print(min(list1))
def digui(a):
    if len(a) == 1 or len(a) == 0:
        return a
    left = []
    right = []
    whe = a[0]
    for i in a[1:]:
        if i > whe:
            right.append(i)
            print(right)
        else:
            left.append(i)
    print(left,right)            
    return digui(left) +  [ whe ]  + digui(right)
print(digui(list1))


#  53.  写一个单列模式

#       因为创建对象时__new__方法执行，并且必须return 返回实例化
#       出来的对象所cls.__instance是否存在，不存在的话就创建对象，
#       存在的话就返回该对象，来保证只有一个实例对象存在（单列），
#       打印ID，值一样，说明对象同一个


class Singleton(object):
    __instance = None
    
    def __new__(cls,age,name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

a = Singleton(18, "dong6e")
b = Singleton(8, "dong6e")

print(id(a))
print(id(b))
a.age  = 19
print(b.age)



#  54.  保留两位小数
#       题目本身只有a="%.03f"%1.3335,让计算a的结果，为了扩充
#       保留小数的思路，提供round方法（数值，保留位数）

a = '%.03f' % 1.3335
print(a,type(a))
b = round(float(a),1)
print(b)
b = round(float(a),2)
print(b)



#  55.  求三个方法打印结果

#       fn("one",1）直接将键值对传给字典；
#       fn("two",2)因为字典在内存中是可变数据类型，所以指向
#       同一个地址，传了新的额参数后，会相当于给字典增加键值
#       对fn("three",3,{})因为传了一个新字典，所以不再是原先默认参数的字典

def fnc(k,v,dict1={}):
    dict1[k]=v
    print(dict1)
fnc('one',1)
fnc('two',2)
fnc('three',3,{})




#  56.  列出常见的状态码和意义

#       200 OK 请求正常处理完毕
#       204 No Content 请求成功处理，没有实体的主体返回
#       206 Partial Content GET范围请求已成功处理
#       301 Moved Permanently 永久重定向，资源已永久分配新URI
#       302 Found 临时重定向，资源已临时分配新URI
#       303 See Other 临时重定向，期望使用GET定向获取
#       304 Not Modified 发送的附带条件请求未满足
#       307 Temporary Redirect 临时重定向，POST不会变成GET
#       400 Bad Request 请求报文语法错误或参数错误
#       401 Unauthorized 需要通过HTTP认证，或认证失败
#       403 Forbidden 请求资源被拒绝
#       404 Not Found 无法找到请求资源（服务器无理由拒绝）
#       500 Internal Server Error 服务器故障或Web应用故障
#       503 Service Unavailable 服务器超负载或停机维护

#  57.  分别从前端、后端、数据库阐述web项目的性能优化

#       该题目网上有很多方法，我不想截图网上的长串文字，
#       看的头疼，按我自己的理解说几点

#       前端优化：

#       1.  减少http请求、例如制作精灵图

#       2.  html和CSS放在页面上部，javascript放在页面下面，
#           因为js加载比HTML和Css加载慢，所以要优先加载html和css,
#           以防页面显示不全，性能差，也影响用户体验差

#       后端优化：


#       1.  缓存存储读写次数高，变化少的数据，比如网站首页的信息、
#           商品的信息等。应用程序读取数据时，一般是先从缓存中读取，
#           如果读取不到或数据已失效，再访问磁盘数据库，并将数据再次写入缓存。

#       2.  异步方式，如果有耗时操作，可以采用异步，比如celery

#       3.  代码优化，避免循环和判断次数太多，如果多个if else判断，
#           优先判断最有可能先发生的情况

#       数据库优化：

#       1.  如有条件，数据可以存放于redis，读取速度快

#       2.  建立索引、外键等



#       58.  使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}

dic={"name":"zs","age":18}
dic.pop('name')
print(dic)
dic={"name":"zs","age":18}
del dic['name']
print(dic)


#  59.  列出常见MYSQL数据存储引擎

#       InnoDB：支持事务处理，支持外键，支持崩溃修复能力和并发控制。
#               如果需要对事务的完整性要求比较高（比如银行），要求
#               实现并发控制（比如售票），那选择InnoDB有很大的优势。
#               如果需要频繁的更新、删除操作的数据库，也可以选择InnoDB，
#               因为支持事务的提交（commit）和回滚（rollback）。

#       MyISAM：插入数据快，空间和内存使用比较低。如果表主要是用于插入
#               新记录和读出记录，那么选择MyISAM能实现处理高效率。如果
#               应用的完整性、并发性要求比 较低，也可以使用。

#       MEMORY：所有的数据都在内存中，数据的处理速度快，但是安全性不高。
#               如果需要很快的读写速度，对数据的安全性要求较低，可以选择
#               MEMOEY。它对表的大小有要求，不能建立太大的表。所以，这类
#               数据库只使用在相对较小的数据库表。


#  60.  计算代码运行结果，zip函数历史文章已经说了，得出[("a",1),("b",2)，("c",3),("d",4),("e",5)]
p = [("a",1),("b",2),("c",3),("d",4),("e",5)]
x = np.array(p).reshape(5,2)
print(x)
t = list(x[...,0])
u = list(x[...,1])
o = list(map(int,u))
A  = list(zip(t,o))
A0 = dict(zip(t,o))
A1 = range(10)
A2 = [ i for i in A1 if i in A0 ]
A3 = [ A0[s] for s in A0 ]
print(t,o)
print(A)
print(A0)
print(A2)
print(A3)

#      dict()创建字典新方法

s = dict([['name','zs'],["age",18]])
print(s)
s = dict([('name','zs'),("age",18)])
print(s)


#  61.  简述同源策略

#       同源策略需要同时满足以下三点要求： 
#       1）协议相同 
#       2）域名相同
#       3）端口相同 
#       http:www.test.com与https:www.test.com 不同源——协议不同
#       http:www.test.com与http:www.admin.com 不同源——域名不同 
#       http:www.test.com与http:www.test.com:8081 不同源——端口不同 
#       只要不满足其中任意一个要求，就不符合同源策略，就会出现“跨域”


#  62.  简述cookie和session的区别

#       1， session 在服务器端，cookie 在客户端（浏览器）

#       2.  session 的运行依赖 session id，而 session id 是
#           存在 cookie 中的，也就是说，如果浏览器禁用了 cookie ，
#           同时 session 也会失效，存储Session时，键与Cookie中的
#           sessionid相同，值是开发人员设置的键值对信息，进行了
#           base64编码，过期时间由开发人员设置

#       3.  cookie安全性比session差

#  63.  简述多线程、多进程

#  进程：
#       1.  操作系统进行资源分配和调度的基本单位，多个进程之间相互独立

#       2.  稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗
#           资源大，开启的进程数量有限制
#  线程：

#       1.  CPU进行资源分配和调度的基本单位，线程是进程的一部分，是比
#           进程更小的能独立运行的基本单位，一个进程下的多个线程可以共
#           享该进程的所有资源

#       2.  如果IO操作密集，则可以多线程运行效率高，缺点是如果一个线程
#           崩溃，都会造成进程的崩溃
#  应用：
#           IO密集的用多线程，在用户输入，
#           sleep 时候，可以切换到其他线程执行，减少等待的时间CPU密集的
#           用多进程，因为假如IO操作少，用多线程的话，因为线程共享一个
#           全局解释器锁，当前运行的线程会霸占GIL，其他线程没有GIL，就不
#           能充分利用多核CPU的优势


#  64.  简述any()和all()方法

#           any():只要迭代器中有一个元素为真就为真
#           all():迭代器中所有的判断项返回都是真，结果才为真
#           python中什么元素为假？
#           答案：（0，空字符串，空列表、空字典、空元组、None, False）

print(bool(0))     #  False
print(bool(""))    #  False
print(bool([]))    #  False
print(bool(()))    #  False
print(bool({}))    #  False
print(bool(None))  #  False

#       测试all()和any()方法

a = [ True , False ]
print(any(a))#  True
print(all(a))#  False

a = ""
print(any(a))  # False

b = ['good','good','good','bad']

print(all(b))  # True

b = ['good','good','good','']

print(all("b"))   #  True
print(any("b"))   #  True
print(all(b))     #  False


#  65.  IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常

#       IOError：输入输出异常
#       AttributeError：试图访问一个对象没有的属性
#       ImportError：无法引入模块或包，基本是路径问题
#       IndentationError：语法错误，代码没有正确的对齐
#       IndexError：下标索引超出序列边界
#       KeyError:试图访问你字典里不存在的键
#       SyntaxError:Python代码逻辑语法出错，不能执行
#       NameError:使用一个还未赋予对象的变量




#  66.  python中copy和deepcopy区别

#  1.  复制不可变数据类型，不管copy还是deepcopy,
#      都是同一个地址当浅复制的值是不可变对象（数值，
#      字符串，元组）时和=“赋值”的情况一样，对象的id值
#      与浅复制原来的值相同。
import copy
a = "哈哈"
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
e = ('a',[1,2])
h = e
f = copy.copy(e)
g = copy.deepcopy(e)
e3 = ('a',1)
h3 = e3
f3 = copy.copy(e3)
g3 = copy.deepcopy(e3)

print(a,id(a))
print(b,id(b))
print(c,id(c))
print(d,id(d))
print(h,id(h))
print(f,id(f))
print(g,id(g))
print(h3,id(h3))
print(f3,id(f3))
print(g3,id(g3))

#  2.  复制的值是可变对象（列表和字典）浅拷贝copy有

#      两种情况：
#      第一种情况：  复制的对象中无复杂子对象，原来值的改变
#                    并不会影响浅复制的值，同时浅复制的值
#                    改变也并不会影响原来的值。原来值的id值与
#                    浅复制原来的值不同。

#      第二种情况：复制的对象 中有复杂子对象（例如列表中的一个子
#                  元素是一个列表)，改变原来的值中的复杂子对象
#                  的值 ，会影响浅复制的值。
#                  深拷贝deepcopy：完全复制独立，包括内层列表和字典

list1 = [1,2,[3,4]]
a =  copy.copy(list1)
b = copy.deepcopy(list1)

print('测试原始数据和copy 和 deepcopy后的结果和id地址')
print('结果表明对于外层的列表来说，三者之间是独立的对象')
print('原始数据和id',list1,id(list1))
print('原始数据和id',a,id(a))
print('原始数据和id',b,id(b))
print('************************************************')
print('测试修改外层简单子对像，也就是修改1或者2')
print('结果表明修改了原始list之后，a和b并没有随之改变，符合我们的正常逻辑，因为三者之间是不同的对象')
list1[0]=10
print('将1改成10结果',list1)
print('将1改成10结果',a)
print('将1改成10结果',b)
print('************************************************')
print('测试修改内层列表的值，也就是测试复杂子对像的值的修改')
print('结果表明浅copy并没有真正的将内层列表（字典）独立拷贝出来，导致修改了list1内层列表（字典）后内层列表（字典）的值也变了')
print('结果表明deepcopy深拷贝可以将内层的列表和(字典)独立拷贝出来，所哟b的内层列表(字典)值不变')
list1[2][0]=5
print('将3的值改成5',list1)
print('将3的值改成5',a)
print('将3的值改成5',b)



#  67.  列出几种魔法方法并简要介绍用途

#       __init__:对象初始化方法
#       __new__:创建对象时候执行的方法，单列模式会用到
#       __str__:当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
#       __del__:删除对象执行的方法
#       __call__:调用对像时执行的方法






#  68.  C:\Users\ry-wu.junya\Desktop>python 1.py 22 33命令行启动程序并传参，print(sys.argv)会输出什么数据？

#       文件名和参数构成的列表
import sys
print(sys.argv)

# ./mianshi,.py 22 33
# ['./mianshi.py', '22', '33']

#  69.  请将[i for i in range(3)]改成生成器

#  生成器是特殊的迭代器，

#       1.  列表表达式的【】改为（）即可变成生成器
#       2.  函数在返回值得时候出现yield就变成生成器，而不是函数了；中括号换成小括号即可，有没有惊呆了

a = ( i for i in range(3))
print(type(a))
for i in range(3):
    print(a.__next__())



#  70.  a = "  hehheh  ",去除收尾空格

a = "  hehheh  "
print(a.strip())

#  71.  举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]

list1=[0,-1,3,-10,5,9]
list1.sort(reverse=False)
print('list.sort 是在list 的基础上修改，无返回值',list1)
list1=[0,-1,3,-10,5,9]
res = sorted(list1,reverse=False)
print('sorted有返回值是新的list',list1)
print('返回值',res)



#  72.  对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序

foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]

a = sorted(foo,key=lambda x:x)
print(a)

#  73.  使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，
#       输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，
#       正数从小到大，负数从大到小（传两个条件，x<0和abs(x)）

foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]

a = sorted(foo,key=lambda x:(x<0,abs(x)))
print(a)

#  74.  列表嵌套字典的排序，分别根据年龄和姓名排序foo = [{"name":"zs","age":19},{"name":"ll","age":54},        {"name":"wa","age":17},{"name":"df","age":23}]
foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]

a = sorted(foo,key=lambda x :x["age"],reverse=False)
print(a)

b = sorted(foo,key=lambda x: x['name'],reverse=False)
print(b)

#  75.  列表嵌套元组，分别按字母和数字排序

foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]
a=[]
b=[]
for i in foo:
    a.append(i['name'])
    b.append(i['age'])
k = list(zip(a,b))

a = sorted(k,key=lambda x:x[0],reverse=False)
print(a)
b = sorted(k,key=lambda x:x[1],reverse=False)
print(b)

    
#  76.  列表嵌套列表排序，年龄数字相同怎么办？
print(k)
a = [ list(i)  for i in k ]
a.append(['xf',23])   
a[1][1]= 23
print(a)
o = sorted(a,key=lambda x:x[1])
print(o)
l = sorted(a,key=lambda x:(x[1],x[0]))
print(l)
t = sorted(a,key=lambda x:x[0])
print(t)

#  77.  根据键对字典排序（方法一，zip函数）

dic = {"name":'zs','sex':'man','city':'bj'}

foo = zip(dic.keys(),dic.values())
print('将字典转换为嵌套元组',foo)
b = sorted(foo,key=lambda x : x[0])
print('根据元组排序',b)
print('重新构造字典',dict(b))


#  78.  根据键对字典排序
#      （方法二,不用zip)有没有发现dic.items和zip(dic.keys(),dic.values())
#       都是为了构造列表嵌套字典的结构，方便后面用sorted()构造排序规则


dic = {"name":'zs','sex':'man','city':'bj'}
foo = dic.items()
print('将字典转换为嵌套元组',foo)
b = sorted(foo,key=lambda x : x[0])
print('根据元组排序',b)
new_dic = { i[0]:i[1] for i in b }
print('字典推导式构造新字典',new_dic)

#  79.  列表推导式、字典推导式、生成器

td_list = [ i for i in range(10)]
print('列表推导式',td_list,type(td_list))

ge_list = ( i for i in range(10) )
print('生成器',ge_list,type(ge_list))

dic = { k:random.randint(4,9) for k in ['a','b','c','d','e']}
print('字典推导式',dic,type(dic))


#  80.  最后出一道检验题目，根据字符串长度排序，看排序是否灵活运用

s = [ 'aa','fff','dssds','a']
print(s)
p = sorted(s,key=lambda x: len(x))
print(p)
s.sort(key=len)
print(s)

#  81.  举例说明SQL注入和解决办法

#       当以字符串格式化书写方式的时候，如果用户输
#       入的有;+SQL语句，后面的SQL语句会执行，比如
#       例子中的SQL注入会删除数据库demo
import pymysql

conn = pymysql.connect(
host = '127.0.0.1',
port = 3306,
user = 'root',
passwd = '',
db = 'nsd1806',
charset = 'utf8',
)

cur = conn.cursor()        # 创建游标
#create1 = 'create table departments(de_ip int(2),name varchar(20))'
#cur.execute(create1)
#conn.commit()
#insert1 = 'insert into departments values(%s,%s)'
#hr = (1,'HR')
#deps = [(2,'运维部'),(3,'开发部'),(4,'财务部')]
#cur.execute(insert1,hr)           # 插入一行记录
#cur.executemany(insert1,deps)     # 插入多行记录
#conn.commit()  
cur.close()
conn.close()

input_name='zs'
sql='select * from demo where name="%s"'  % input_name
print('正常SQL语句',sql)

input_name='zs;drop database demo'
sql='select * from demo where name "%s"'   % input_name
print('sql 注入语句',sql)



#    解决方式：   通过传参数方式解决SQL注入
#params = [ input_name ]
#count = cs1.execute('select * from goods where name=%s', params)


#  82.  s="info:xiaoZhang 33 shandong",用正则切分字符
#       串输出['info', 'xiaoZhang', '33', 'shandong']

#        |表示或，根据冒号或者空格切分

s="info:xiaoZhang 33 shandong"

res = re.split(r":| ",s)

print(res)

#  83.  正则匹配以163.com结尾的邮箱
 
m =['m13268275527@163.com', '13268275527@163.com' , 'm98030902@qq.com']

for i in m:
    res = re.search(r'@163\.com$',i)
    if res:
        print('%s 是正确的邮箱' % i)
    else:
        print('%s 不是正确的邮箱' % i)





#  84.  递归求和

def qiuhe(num):
    if  num > 0:
        return  num  + qiuhe(num-1)    
    else: 
        return num
print(qiuhe(100))    

#  85.  python字典和json字符串相互转化方法

#       json.dumps()字典转json字符串，json.loads()json转字典
import json
dic = {"name": "zs"}
res = json.dumps(dic)
print(res,type(res))
ret = json.loads(res)
print(ret,type(ret))



#  86.  MyISAM 与 InnoDB 区别：

#  1.  InnoDB 支持事务，MyISAM 不支持，这一点是非常之重要。
#      事务是一种高级的处理方式，如在一些列增删改中只要哪
#      个出错还可以回滚还原，而 MyISAM就不可以了；

#  2.  MyISAM 适合查询以及插入为主的应用，InnoDB 适合频繁修
#      改以及涉及到安全性较高的应用；

#  3.  InnoDB 支持外键，MyISAM 不支持；

#  4.  对于自增长的字段，InnoDB 中必须包含只有该字段的索引，
#      但是在 MyISAM表中可以和其他字段一起建立联合索引；

#  5.  清空整个表时，InnoDB 是一行一行的删除，效率非常慢。MyISAM 则会重建表；


#  87.  统计字符串中某字符出现次数

str1 = 'asssffssafes'

res = str1.count('s')
print(res)
#  88.  字符串转化大小写

str1 = 'HHHuuu'

print(str1.upper())
print(str1.lower())

#  89.  用两种方法去空格

str1 = ' hello world haha '

res = str1.replace(' ','')
print(res)

list1 = str1.split(' ')
res = ''.join(list1)
print(res)

#  90.  正则匹配不是以4和7结尾的手机号


tels = [ '1332589652','1332589654','1332589657','1332589652' ]

for i in tels:
    res = re.search(r'[^47]$',i) 
    if res:
        print('想要的结果 %s ' % i)
    else:
        print('不想要的结果 %s' % i)



#  91.  简述python引用计数机制

#       python垃圾回收主要以引用计数为主，标记-清除和分代清除
#       为辅的机制，其中标记-清除和分代回收主要是为了处理循环
#       引用的难题。


#       引用计数算法
#       当有1个变量保存了对象的引用时，此对象的引用计数就会加1
#       当使用del删除变量指向的对象时，如果对象的引用计数不为1，
#       比如3，那么此时只会让这个引用计数减1，即变为2，当再次
#       调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除

import time 

class Animal(object):

    def __init__(self, name):
        print('__init__ 方法被调用')
        self.name = name 

    def __del__(self):
        print('__del__方法被调用')
        print('%s 对像要被干掉了...' % self.name )

cat = Animal('波斯猫')
cat1 = cat
cat2 = cat
print(id(cat),id(cat),id(cat))
print('删除 cat对象')
del cat
print('删除 cat1对象')
del cat1
print('删除 cat2对象')
del cat2
print('程序两秒中后 结束')
#time.sleep(2)


#  92.  int("1.4"),int(1.4)输出结果？

#   int("1.4")报错，int(1.4)输出

#  93.  列举3条以上PEP8编码规范

#  1.  顶级定义之间空两行，比如函数或者类定义。
#  2.  方法定义、类定义与第一个方法之间，都应该空一行
#  3.  三引号进行注释
#  4.  使用Pycharm、Eclipse一般使用4个空格来缩进代码


#  94.  正则表达式匹配第一个URL
#       findall结果无需加group(),search需要加group()提取

s = '<img class="default-logo" src="http://cdn.tmooc.cn/tmooc-web/css/img/tmooc-logo.png"/> <img class="blue-logo" src="http://cdn.tmooc.cn/tmooc-web/css/img/tmooc-logo2.png"/>'

res = re.findall(r'http://.*?.png',s)
print(res[0])
ret = re.search(r'http://.*?png',s)
print(ret.group())


#  95.  正则匹配中文


title = '你好 , hello , 世界'

patt = re.compile(r'[\u4e00-\u9fa5]+')

res = patt.findall(title)

print(res)

#  96.  简述乐观锁和悲观锁

#       悲观锁, 就是很悲观，每次去拿数据的时候都认为别人会修改，
#       所以每次在拿数据的时候都会上锁，这样别人想拿这个数据就会
#       block直到它拿到锁。传统的关系型数据库里边就用到了很多这种
#       锁机制，比如行锁，表锁等，读锁，写锁等，都是在做操作之前先上锁。

#       乐观锁，就是很乐观，每次去拿数据的时候都认为别人不会修改，
#       所以不会上锁，但是在更新的时候会判断一下在此期间别人有没
#        有去更新这个数据，可以使用版本号等机制，乐观锁适用于多
#       读的应用类型，这样可以提高吞吐量

#  97.  r、r+、rb、rb+文件打开模式区别模式较多，比较下背背记记即可

#    访问模式            说明
#    r         以只读的方式打开文件，文件的指针会放在文件的开头，这
#              是默认的方式

#    w         打开一个文件只用于写入，如果文件以存在则将其覆盖，如
#              如果文件不存在则将其创建

#    a         打开一个文件用于追加，如果文件以存在则文件指针将会放在
#              文件末尾，也就是说，新的内容将会被写入，到已有的内容之
#              后如果文件不存在则创建新文件将其写入。

#    rb        以二进制格式打开一个文件用于文件的指针会放在文件的开头，这
#              是默认的方式

#    wb        以二进制格式 打开一个文件只用于写入，如果文件以存在则将其覆盖，如
#              如果文件不存在则将其覆盖

#    ab        以二进制打开一个文件用于追加，如果文件以存在则文件指针将会放在
#              文件末尾，也就是说，新的内容将会被写入，到已有的内容之
#              后如果文件不存在则创建新文件将其写入。

#    r+        以读写的方式打开文件，文件的指针会放在文件的开头

#    w+        以读写的方式打开文件如果文件以存在则将其覆盖，如
#              如果文件不存在则将其创建

#    a+        以读写的方式打开文件，文件的指针会放在文件的末尾
#              打开文件时是追加模式，如果文件不存在则将其创建

#    rb+        以二进制格式 读写的方式打开文件，文件的指针会放在文件的开头

#    wb+        以二进制格式 读写的方式打开文件如果文件以存在则将其覆盖，如
#              如果文件不存在则将其创建

#    ab+        以二进制格式 读写的方式打开文件，文件的指针会放在文件的末尾
#              打开文件时是追加模式，如果文件不存在则将其创建


#  98.  Linux命令重定向 

#              > 和 >>Linux 允许将命令执行结果 重定向到一个 文件将本应显示
#              在终端上的内容 输出／追加 到指定文件中> 表示输出，会覆盖文件
#              原有的内容>> 表示追加，会将内容追加到已有文件的末尾用法
#              示例：将 echo 输出的信息保存到 1.txt 里echo Hello Python > 
#               1.txt将 tree 输出的信息追加到 1.txt 文件的末尾tree >> 1.txt


#  99.  正则表达式匹配出<html><h1>www.itcast.cn</h1></html>前面的<>
#       和后面的<>是对应的，可以用此方法

labels = [ '<html><h1>www.itcast.cn</h1></html>','<html><h1>www.itcast.cn</h2></html>' ]

for i in labels:
    res = re.search(r'<(\w+)><(\w+)>.*</\2></\1>',i)
    if res:
        print('%s  是符合规则的' % res.group())
    else:
        print('%s 是不符合规则的' % res)



#  100.  python传参数是传值还是传址？

#        Python中函数参数是引用传递（注意不是值传递）。
#        对于不可变类型（数值型、字符串、元组），因变量不能修改，
#        所以运算不会影响到变量自身；而对于可变类型（列表字典）来说，
#        函数体运算可能会更改传入的参数变量。

def selfta(a):
    a += a

a_int = 1
print(a_int)
selfta(a_int)
print(a_int)
a_list = [ 1, 2 ]
print(a_list)
selfta(a_list)
print(a_list)

#  1
#  1
#  [1, 2]
#  [1, 2, 1, 2]





#  101.  求两个列表的交集、差集、并集 

a = [ 1 , 2 , 3 , 4 ]
b = [ 4 , 3 , 5 , 6 ]

a = set(a)
b = set(b)
print(a-b)
print(a&b)
print(a|b)



#  102.  生成0-100的随机数
#        random.random()生成0-1之间的随机小数，所以乘以100

res1 = random.randint(1,100)
res2 = 100*random.random()
res3 = random.choice(range(0,101))
print(res1)
print(res2)
print(res3)

#  103.  lambda匿名函数好处精简代码，
#        lambda省去了定义函数，map省去了写for循环过程


a = [ '苏州', '中国','哈哈', '', '' , '日本' , '' , '' ,'德国' ]

res = list(map(lambda x :'填充物' if x == '' else x , a))

print(res)


#  104.  常见的网络传输协议


#        UDP、TCP、FTP、HTTP、SMTP等等



#  105.  单引号、双引号、三引号用法

#  1.  单引号和双引号没有什么区别，不过单引号不用按shift，
#      打字稍微快一点。表示字符串的时候，单引号里面可以用
#      双引号，而不用转义字符,反之亦然。
#      'She said:"Yes." '   or  "She said: 'Yes.' "
#  2.  但是如果直接用单引号扩住单引号，则需要转义，
#      像这样： ' She said:\'Yes.\' '

#  3.  三引号可以直接书写多行，通常用于大段，

#      大篇幅的字符串
"""
helloworld"""


#  106.  python垃圾回收机制

#        python垃圾回收主要以引用计数为主，标记-清除和分代清除为辅的机制，
#        其中标记-清除和分代回收主要是为了处理循环引用的难题。

#       引用计数算法当有1个变量保存了对象的引用时，此对象的引用计数
#       就会加1当使用del删除变量指向的对象时，如果对象的引用计数不为
#       1，比如3，那么此时只会让这个引用计数减1，即变为2，当再次调用
#       del时，变为1，如果再调用1次del，此时会真的把对象进行删除


#  107.  HTTP请求中get和post区别

#  1.  GET请求是通过URL直接请求数据，数据信息可以在URL中直接看到，比如浏览器访问；而POST请求是放在请求头中的，我们是无法直接看到的；
#  2.  GET提交有数据大小的限制，一般是不超过1024个字节，而这种说法也不完全准确，HTTP协议并没有设定URL字节长度的上限，而是浏览器做了些处理，所以长度依据浏览器的不同有所不同；POST请求在HTTP协议中也没有做说明，一般来说是没有设置限制的，但是实际上浏览器也有默认值。总体来说，少量的数据使用GET，大量的数据使用POST。
#  3.  GET请求因为数据参数是暴露在URL中的，所以安全性比较低，比如密码是不能暴露的，就不能使用GET请求；POST请求中，请求参数信息是放在请求头的，所以安全性较高，可以使用。在实际中，涉及到登录操作的时候，尽量使用HTTPS请求，安全性更好。
#  108.  python中读取Excel文件的方法应用数据分析库pandas

import pandas as pd 
df = pd.read_excel('3.xlsx')
print(dict(df))
#  109.  简述多线程、多进程进程：
#  1.  操作系统进行资源分配和调度的基本单位，多个进程之间相互独立
#  2.  稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗资源大，开启的进程数量有限制线程：
#  1.  CPU进行资源分配和调度的基本单位，线程是进程的一部分，是比进程更小的能独立运行的基本单位，一个进程下的多个线程可以共享该进程的所有资源
#  2.  如果IO操作密集，则可以多线程运行效率高，缺点是如果一个线程崩溃，都会造成进程的崩溃应用：IO密集的用多线程，在用户输入，sleep 时候，可以切换到其他线程执行，减少等待的时间CPU密集的用多进程，因为假如IO操作少，用多线程的话，因为线程共享一个全局解释器锁，当前运行的线程会霸占GIL，其他线程没有GIL，就不能充分利用多核CPU的优势
#  110.  python正则中search和match

