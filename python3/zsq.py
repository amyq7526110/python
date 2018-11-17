#!/usr/bin/env python3



#     装饰器
#     •  装饰器是在函数调用之上的修饰
#     •  这些修饰仅是当声明一个函数或者方法的时候,才会
#     应用的额外调用
#     •  使用装饰器的情形有:
#     –  引入日志
#     –  增加计时逻辑来检测性能
#     –  给函数加入事务的能力


def set_color(func):
    def color():
        return "\033[31m%s\033[0m" % func()
    return color
def hello():
    return "Hello World"
@set_color
def greet():
    return "How are you"
if __name__ == '__main__':
#    print(color(hello))
#    print(greet())
#     a = set_color(hello)
#     print(a())
     hello = set_color(hello)
     print(hello())
     print(greet())


  
