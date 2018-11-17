#!/usr/bin/env python3

import tkinter 
from functools import partial 
#  内部函数

#  闭包

#  •  闭包将内部函数自己的代码和作用域以及外部函数的
#  作用结合起来

#  •  闭包的词法变量不属于全局名字空间域或者局部的--
#  而属于其他的名字空间,带着“流浪"的作用域

#  •  闭包对于安装计算,隐藏状态,以及在函数对象和作
#  用域中随意地切换是很有用的

#  •  闭包也是函数,但是他们能携带一些额外的作用域

#  闭包实例

#  •  创建通用的计数器

def welcome(word):
   def say_hi():
       lb.config(text='Hello %s' % word)
   return say_hi
root = tkinter.Tk()
lb = tkinter.Label(text='Hello World', font='Arial, 30')
MyButton =  partial(tkinter.Button,root,fg='white',bg='blue')
b1 = MyButton(text='Button 1',command=welcome('Tedu'))
b2 = MyButton(text='Button 2',command=welcome('China'))
b3 = MyButton(text='Quit',command=root.quit)
for item in [lb,b1,b2,b3]:
    item.pack()
root.mainloop()



