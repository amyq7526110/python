#!/usr/bin/env python3
import os
import sys
#   open及file内建函数

#   •  作为打开文件之门的“钥匙”,内建函数open()以及
#   file()提供了初始化输入/输出(I/O)操作的通用接口

#   •  成功打开文件后时候会返回一个文件对象,否则引发一个错误

#   •  open()方法和file()方法可以完全相互替换

#   •  基本语法:

#   file_object=open(file_name,	access_mode='r',buffering=-1)	

fobj = open('test.txt')
print(fobj)
fobj.close()

# <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>


#   文件对象访问模式

#   文件模式    操作

#   r           以读方式打开(文件不存在则报错)
#   w           以写方式打开(文件存在则清空,不存在则创建)
#   a           以追加模式打开(必要时创建新文件)
#   r+          以读写模式打开(参见r)
#   w+          以读写模式打开(参见w)
#   a+          以读写模式打开(参见a)
#   b           以二进制模式打开

# ff =  open('haha')

# FileNotFoundError: [Errno 2] No such file or directory: 'haha'


ff = open('haha','w')

ff.close()

#  不报错


ffo = open('test.txt','r')

#  read()

#  read方法
#  •  read()方法用来直接读取字节到字符串中,最多读取给定数目个字节

#  •  如果没有给定size参数(默认值为-1)或者size值为-1,文件将被读取直至末尾

#  >>>	dataReceived(=	fobj.read()	
#  >>>	print(data)	

data = ffo.read()
print(data)
data = ffo.read()
print(data)
ffo.close()

#  read() 使用指针进行文件的读取

#  读取全部内容之后，指针移动到最后

#  readline方法

#  •  读取打开文件的一行(读取下个行结束符之前的所有字节)
#  •  然后整行,包括行结束符,作为字符串返回
#  •  它也有一个可选的size参数,默认为-1,代表读至结束符'\n'
#  •  如果提供了该参数,那么在超过size个字节后会返回不完整的行

#  >>>	dataReceived(=	fobj.readline()	
#  >>>	print(data)	readlines方法

#  readlines()方法

#    读取所有(剩余的)行然后把它们作为一个字符串列表返回

#  >>>	dataReceived(=	fobj.readlines()	
#  >>>	print(data)	

f = open('test')
print(f.read(5))
print(f.readline())
print(f.readline(5))
print(f.readline())
print(f.readlines())
f.close()


#   write方法

#   •  write()内建方法功能与read()和readline()相反。它
#   把含有文本数据或二进制数据块的字符串写入到文件
#   中去

#   •  写入文件时,不会自动添加行结束标志,需要程序员
#   手工输入

#   >>>	fobj.write('HelloWorld!\n')	

wf = open('haha','w')
wf.write('hello world\n')
wf.write('ni hao\n')
wf.close()
os.system('cat haha')

#   writelines方法
#   •  和readlines()一样,writelines()方法是针对列表的操作
#   •  它接受一个字符串列表作为参数,将它们写入文件
#   •  行结束符并不会被自动加入,所以如果需要的话,必
#   须在调用writelines()前给每行结尾加上行结束符

#   >>>	fobj.writelines(['HelloWorld!\n','pythonrcprograming\n'])

data =  ['newline\n','twoline\n']
wwf = open('lele','w')
wwf.writelines(data)
wwf.close()
os.system('cat lele')

#  with 

#  •  with语句是用来简化代码的
#  •  在将打开文件的操作放在with语句中,代码块结束后,文件将自动关闭

#  >>>	with  open('foo.py') as f:	
#           data=f.readlines()	
#  >>>	f.closed
#  True

with open('haha') as fff:
    print(fff.read())
print(f.closed)

#   文件内移动
#   •  seek(offset[, whence]):移动文件指针到不同的位置
#   –  offset是相对于某个位置的偏移量
#   –  whence的值,0表示文件开头,1表示当前位置,2表
#   示文件的结尾
#   •  tell():返回当前文件指针的位置

with open('test') as h:
    print(h.tell())
    print(h.read(100))
    print(h.tell()) 
with open('haha') as ha:
    print(ha.tell())
    print(ha.seek(0,2))
    print(ha.tell())
with open('haha') as ha:
    print(ha.read())
    print(ha.seek(0,0))
    print(ha.read())

#   文件迭代
#   •  如果需要逐行处理文件,可以结合for循环迭代文件
#   •  迭代文件的方法与处理其他序列类型的数据类似
#   >>>	fobj =	open('star.py')	
#   >>>	for eachLine in fobj:	
#   	print(eachLine,end='')	


with open('haha') as stt:
    for i in stt:
        print(i,end='')


#    标准文件
#    •  程序一执行,就可以访问三个标准文件
#    –  标准输入:一般是键盘,使用sys.stdin
#    –  标准输出:一般是显示器缓冲输出,使用sys.stdout
#    –  标准错误:一般是显示器的非缓冲输出,使用sys.stderr


sys.stdout.write('hello world\n')

#  cp 

bi = open('/bin/ls','rb')
ro = open('/root/ls','wb')
while True:
    date = bi.read(4096) 
    if  not date:
        break
    ro.write(date) 
ro.close()
bi.close()

#  读取文件加一定的限制

with open('test','rb') as qy:
     qy.seek(-20,2)
     print(qy.read())

