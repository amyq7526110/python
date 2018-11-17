#!/usr/bin/env python3
import sys

   #  函数基本概念

   #  •  函数是对程序逻辑进行结构化或过程化的一种编程方法
   #  •  将整块代码巧妙地隔离成易于管理的小块
   #  •  把重复代码放到函数中而不是进行大量的拷贝,这样
   #     既能节省空间,也有助于保持一致性
   #  •  通常函数都是用于实现某一种功能

   #     创建函数

   #     •  函数是用def语句来创建的,语法如下:

   #     def funcOon_name(arguments):（def 函数名(参数列表)）	
   #  	     "funcOon_documentaOon_string"(文档字符串 说明参数的使用help(print))
   #         funcOon_body_suite

   #  •  标题行由def关键字,函数的名字,以及参数的集合(如果有的话)组成
   #  •  def子句的剩余部分包括了一个虽然可选但是强烈推
   #  	 荐的文档字串,和必需的函数体

   #   调用函数
   #   •  同大多数语言相同,python用一对圆括号调用函数
   #   •  如果没有加圆括号,只是对函数的引用

def foo():
    print('hello world')
foo()    # 调用函数
print(foo)
# <function foo at 0x7fdef0784ea0> 查找函数对象

   #   函数的返回值
   #   •  多数情况下,函数并不直接输出数据,而是向调用者
   #   返回值
   #   •  函数的返回值使用return关键字
   #   •  没有return的话,函数默认返回None


def fzz():    
    res = 3+4  # 相当于shell 的 local 定义变量
    return res 
print(fzz())     # 7
print(fzz()*2)   # 14 

     
    #  函数参数

    #  定义参数

    #  •  形式参数

    #  –  函数定义时,紧跟在函数名后(圆括号内)的参数被
    #  称为形式参数,简称形参。由于它不是实际存在变量,
    #  所以又称虚拟变量
    #  形参

    #  •  实际参数

    #  –  在主调函数中调用一个函数时,函数名后面括弧中的
    #  参数(可以是一个表达式)称为“实际参数”,简称
    #  实参
 
    #  传递参数
    #  •  调用函数时,实参的个数需要与形参个数一致
    #  •  实参将依次传递给形参

def febo(x):
    fibo = [0,1 ]
    for i in range(x-2):
        fibo.append(fibo[-1]+fibo[-2])
    print(fibo) 
febo(6)
febo(10)
    # 位置参数
    # •  与shell脚本类似,程序名以及参数都以位置参数的方
    # 式传递给python程序
    # •  使用sys模块的argv列表接收

print(sys.argv)

#def cp_file():
#    src_obj = open(sys.argv[1],'rb')
#    dest_obj = open(sys.argv[2],'wb')
#    while True:
#        data = src_obj.read(4096)
#	if not data:
#	    break 
#	dest_obj.write(data)
#    src_obj.close()
#    dest_obj.close()
#     
#cp_file()


#       默认参数
#       •  默认参数就是声明了默认值的参数
#       •  因为给参数赋予了默认值,所以在函数调用时,不向
#       该参数传入值也是允许的

def pater(num=30):
    print('*'*num)
pater()
pater(10)












