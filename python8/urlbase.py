#!/usr/bin/env python3

#  urllib简介

#  •  在Python2版本中,有urllib和urlib2两个库可以用来
#  实现request的发送。而在Python3中,已经不存在
#  urllib2这个库了,统一为urllib

#  •  urllib中包括了四个模块

#  –  urllib.request可以用来发送request和获取request的结果
#  –  urllib.error包含了urllib.request产生的异常
#  –  urllib.parse用来解析和处理URL
#  –  urllib.robotparse用来解析页面的robots.txt文件

#  爬取网页

#  •  先需要导入用到的模块:urllib.request
#  •  在导入了模块之后,我们需要使用
#  urllib.request.urlopen打开并爬取一个网页
#  •  读取内容常见的有3种方式:
#  –  read()读取文件的全部内容,与readlines()不同的是,
#  read()会把读取到的内容赋给一个字符串变量。
#  –  readlines()读取文件的全部内容,readlines()会把读
#  取到的内容赋值给一个列表变量。
#  –  readline()读取文件的一行内容。
