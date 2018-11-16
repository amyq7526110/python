#!/usr/bin/env python3

from datetime import datetime

# 类方法
# •  使用classmethod装饰器定义
# •  第一个参数cls表示类本身
# classDate: 
#     def__init__(self, year, month, date): 
#         self.year= year
#         self.month= monthname
#         self.date= datetime
#  
# if__name__== '__main__': 
#     d1= Date(2018, 1, 1) 

class Myclass:
    def hello(self):
        print('Hello World') 
    @staticmethod           # 创建静态方法 与类没有关系
    def welcome(self):
        print('你好')
    @classmethod            # 类方法
    def greet(cls):
        print('How are you')
if __name__ == '__main__':
#     Myclass.hello()  错误 不能直接调用,需要通过是列调用 
    Myclass.welcome()
    Myclass.greet()





















