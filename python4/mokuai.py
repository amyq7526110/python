#!/usr/bin/env python3

import randpass

# 模块和文件

#  
#  什么是模块

#  •  模块支持从逻辑上组织python代码
#  •  当代码量变得相当大的时候, 最好把代码分成一些有
#  组织的代码段
#  •  代码片段相互间有一定的联系,可能是一个包含数据
#  成员和方法的类,也可能是一组相关但彼此独立的操
#  作函数
#  •  这些代码段是共享的,所以python允许“调入”一
#  个模块,允许使用其他模块的属性来利用之前的工作
#  成果,实现代码重用

#  模块文件
#  •  说模块是按照逻辑来组织python代码的方法,文件
#  是物理层上组织模块的方法
#  •  一个文件被看作是一个独立模块,一个模块也可以被
#  看作是一个文件
#  •  模块的文件名就是模块的名字加上扩展名.py


print(randpass.randpass(10))       # 调用函数
print(randpass.all_chs)            # 只能调用randpass中的全局变量

#  import 99  错误



#   名称空间

#   •  名称空间就是一个从名称到对象的关系映射集合
#   •  给定一个模块名之后,只可能有一个模块被导入到
#   python解释器中,所以在不同模块间不会出现名称交
#   叉现象
#   •  每个模块都定义了它自己的唯一的名称空间

import foo
import bar
print(foo.hi())        # hello
print(bar.hi())        # great


#  导入模块


#  搜索路径

#  •  模块的导入需要一个叫做“路径搜索”的过程
#  •  python在文件系统“预定义区域”中查找要调用的模块
#  •  搜索路径在sys.path中定义


import sys

print(sys.path)

# ['/root/python/python4', '/usr/local/lib/python36.zip', '/usr/local/lib/python3.6', '/usr/local/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']


#  用户自定义的模块可以放在site-packages 下 或用 环境变量PYTHONPSTH 定义




#   模块导入方法

#   •  使用import导入模块
#   •  可以在一行导入多个模块,但是可读性会下降
#   •  可以只导入模块的某些属性
#   •  导入模块时,可以为模块取别名

#  >>> importDme, os, sys
#  >>> from random import choice
#  >>> import pickle as p



#   导入和加载

#   •  当导入模块时,模块的顶层代码会被执行

#   •  一个模块不管被导入(import)多少次,只会被加
#   载(load)一次

#  [root@py01~] cat foo.py
#  hi = 'hello' 
#  print(hi) 
#  [root@py01~] python3
#  >>> importfoo
#  Hello           #第一次导入,执行print语句
#  >>> import foo  #再次导入,print语句不再执行 

#  从zip文件中导入
#  •  在2.3版中,python加入了从ZIP归档文件导入模块
#  的功能
#  •  如果搜索路径中存在一个包含python模块(.py、.pyc、
#  或.pyo文件)的.zip文件,导入时会把ZIP文件当作目
#  录处理



#  导入sys模块,在搜索路径中加入相应的zip文件 

# >>> import sys
# >>> sys.path.append('/root/pymodule.zip') 
# >>> import foo

#  导入pymodule.zip压缩文件中的foo模块 


#  包

#  目录结构
#  •  包是一个有层次的文件目录结构,为平坦的名称空间
#  加入有层次的组织结构
#  •  允许程序员把有联系的模块组合到一起
#  •  包目录下必须有一个__init__.py文件

#  绝对导入
#  •  包的使用越来越广泛,很多情况下导入子包会导致和
#  真正的标准库模块发生冲突
#  •  因此,所有的导入现在都被认为是绝对的,也就是说
#  这些名字必须通过python路径(sys.path或
#  PYTHONPATH)来访问

#  相对导入
#  •  绝对导入特性使得程序员失去了import的自由,为
#  此出现了相对导入
#  •  因为import语句总是绝对导入的,所以相对导入只
#  应用于from-import语句


#  内置模块

#  hashlib模块
#  •  hashlib用来替换md5和sha模块,并使他们的API一
#  致,专门提供hash算法
#  •  包括md5、sha1、sha224、sha256、sha384、
#  sha512,使用非常简单、方便
#  >>>  importhashlib
#  >>>  models=  hashlib.md5()  
#  >>>  m.update('helloworld!')  
#  >>>  m.hexdigest()  
#  'fc3ff98e8c6a0d3087d515c0473f8677'  







