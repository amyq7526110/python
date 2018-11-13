#!/usr/bin/env python3
import keyword


   #    语法风格

    
#  python支持链式多重赋值
x = y = 10
print(x,y)

#  另一种将多个变量同时赋值的方法称为多元赋值,采    
#  用这种方式赋值时,等号两边的对象都是元组
a, b = [10,30], [20,40]
print('a =',a,'b =',b)

#  注意变量和值的个数及顺序

a, b = b, a
print('a =',a,'b =',b)

c = [10,20]
print(c)
c[0],c[1] = c[1],c[0] 
print(c)


#  合法标识符

#    python标识符字符串规则和其他大部分用C编写的高
#    级语言相似

#    第一个字符必须是字母或下划线(_)

#    剩下的字符可以是字母和数字或下划线

#    大小写敏感



#    关键字

#      和其他的高级语言一样,python也拥有一些被称作
#    关键这字的保留字符

#      任何语言的关键字应该保持相对的稳定,但是因为
#    python是一门不断成长和进化的语言,其关键字偶
#    尔会更新

#      关键字列表和iskeyword()函数都放入了keyword模
#    块以便查阅

print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print(keyword.iskeyword('name'))
#False
print(keyword.iskeyword('if'))
#True

#  内建
#    除了关键字之外,python还有可以在任何一级代码
#  使用的“内建”的名字集合,这些名字可以由解释器
#  设置或使用
#    虽然built-in不是关键字,但是应该把它当作“系统
#  保留字”
#    保留的常量如:True、False、None


#  模块结构及布局

#    编写程序时,应该建立一种统一且容易阅读的结构,
#    并将它应用到每一个文件中去

 #!/usr/bin/environpython#起始行
 #  “thishost(isatestmodule”	#模块文档字符串
 #import   sys                  #导入模块
 #import   os
 #debug=True                    #全局变量声明
 #classFooClass(object):        #类定义
 #    'FooClass class'	
 #  pass
 #def  test():         	        #函数定义
 #    "test function"	
 #   foo=FooClass()	
 #if__name__==‘__main__’:	#程序主体
 #    test()	


