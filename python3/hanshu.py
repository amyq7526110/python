#!/usr/bin/env python3

# 创建函数

#  def 语句
#  •  函数用def语句创建,语法如下:
#  deffunc(on_name(arguments): 
#      "func(on_documenta(on_string" 
#      func(on_body_suite
#  •  标题行由def关键字,函数的名字,以及参数的集合
#  (如果有的话)组成
#  •  def子句的剩余部分包括了一个虽然可选但是强烈推
#  荐的文档字串,和必需的函数体

#  前向引用
#   •  函数不允许在函数未声明之前对其进行引用或者调用

#  deffoo(): 
#      print('infoo') 
#      bar() 
#   
#  foo()              #报错,因为bar没有定义
#  -------------------------------------------------------------------- 
#  deffoo(): 
#      print('infoo') 
#      bar() 
#   
#  defbar(): 
#      print('inbar’) 
#  foo()             #正常执行,虽然bar的定义在foo定义后面


#  内部函数
#  •  在函数体内创建另外一个函数是完全合法的,这种函
#  数叫做内部/内嵌函数

#   关键字参数
#   •  关键字参数的概念仅仅针对函数的调用
#   •  这种理念是让调用者通过函数调用中的参数名字来区
#   分参数
#   •  这样规范允许参数缺失或者不按顺序


def set_info(name,age):
    print('%s is %s years old' % (name,age))
set_info('bob',16)          #  bob is 16 years old
set_info(16,'bob')          # 没有语法错误，语义有错误 16 is bob years old
#set_info(age=16,'bob')     # 语法错误
#set_info(16,name='bob')    # name 两个值 错误

set_info(age=16,name='bob')  # ok bob is 16 years old
#set_info(age=16,name='bob',age=16)  # 


#  def bar(): 
#      print('bar() iscalled') 
#  .
#  >>> foo() 
#  foo() is called
#  bar() is called
#  >>> bar() 

#  函数操作符
#  •  使用一对圆括号()调用函数,如果没有圆括号,只是
#  对函数的引用
#  •  任何输入的参数都必须放置在括号中
    

#   参数组
#   •  python允许程序员执行一个没有显式定义参数的函数
#   •  相应的方法是通过一个把元组(非关键字参数)或字
#   典(关键字参数)作为参数组传递给函数
#   
def mytest(*args):               # *表示args是一个元祖
    print(args)
mytest(10,20,'dsfa')

def mytest2(**kwargs):            # **表示是一个字典
    print(kwargs)
mytest2(name='zs',age=16)

user = ['alise',24]

# set_info(user)                 #  报错,name=user age 没有值

set_info(*user)                  #  调用时 *把user列表拆开 
                                 #  alise is 24 years old





















