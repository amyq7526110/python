#!/usr/bin/env python3
import tkinter 
from functools import partial 
root = tkinter.Tk()
lb = tkinter.Label(text='Hello World')
b1 = tkinter.Button(root,fg='white',bg='blue',text='Button 1')
MyButton =  partial(tkinter.Button,root,fg='white',bg='blue')
b2 = MyButton(text='Button 2')
b3 = MyButton(text='Quit',command=root.quit)
for item in [lb,b1,b2,b3]:
    item.pack()
root.mainloop()

# yum -y install tcl-devel tk-devel  sqlite-devel

# 



