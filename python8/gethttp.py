#!/usr/bin/env python3

# 万维网与HTTP

# HTTP概述

# •  超文本传输协议(HTTP,HyperText Transfer
# Protocol)是互联网上应用最为广泛的一种网络协议。
# 所有的WWW文件都必须遵守这个标准。设计HTTP
# 最初的目的是为了提供一种发布和接收HTML页面的
# 方法。

# •  HTTP是一个客户端和服务器端请求和应答的标准。
# 客户端是终端用户,服务器端是网站。通过使用Web
# 浏览器、网络爬虫或者其它的工具,客户端发起一个
# 到服务器上指定端口(默认端口为80)的HTTP请求。

#  HTTP工作过程
#  •  客户端发起一个请求,建立一个到服务器指定端口
#  (默认是80端口)的连接

#  •  服务器则在那个端口监听客户端发送过来的请求。一
#  旦收到请求,服务器(向客户端)发回一个状态行,
#  比如"HTTP/1.1 200 OK",和(响应的)消息

#  •  消息的消息体可能是请求的文件、错误消息、或者其
#  它一些信息

#  •  HTTP使用TCP协议



# HTTP消息详解

# 请求和响应
# •  客户端向服务器发送获取文档的请求(request)
# •  一旦发送完请求,客户端就会进行等待,直到从服务
# 器接收到完整的响应(response)为止
# •  当前最流行的HTTP 1.4版本的协议中,不允许客户
# 端在尚未收到上一个请求前就在同一个套接字上开始
# 发送第二个请求


#  请求和响应(续1)
#  GET/ipow(HTTP/1.1# 请求 
#  User-Agent: curl/7.35.0
#  Host:   localhost:8000
#  Accept: */* 
#      
#  HTTP/1.1200OK#  响应    
#  Server: gunicorn/19.1.1
#  Date:   Sat,    20Sep201400:18:00GMT
#  ConnecNon:  close(
#  Content-Type:   applicaNon/json
#  Content-Length: 27
#  Access-Control-Allow-Origin:    *   
#  Access-Control-Allow-CredenNals:    true

#  请求和响应(续2)

#  •  第一行包含一个方法名和要请求的文档名;在响应消息中,
#  第一行包含了返回码和描述消息。无论是在请求和响应消
#  息中,第一行都以回车和换行(CR-LF)结尾

#  •  第二部分包含零或多个头信息,每个头信息由一个名称,
#  一个冒号以及一个值组成。HTTP头的名称区分大小写。
#  头信息之后要再跟上一个空行

#  •  第三部分是一个可选的消息体。消息体紧跟着头信息后面
#  的空行



#  HTTP方法

#  •  GET和POST这两种方法提供了HTTP基本的“读”和“写”操作

#  –  GET    请求获取Request-URI所标识的资源
#  –  POST   在Request-URI所标识的资源后附加新的数据

#  •  其余方法可以分为两大类:本质上类似于GET的方法和本
#  质上类似于POST的方法

#  
#  HTTP方法(续1)
#  •  OPTIONS 请求与给定路径匹配的HTTP头的值
#  •  HEAD 请求服务器做好一切发送资源的准备,但是只发送
#  头信息
#  •  DELETE 请求服务器删除Request-URI所标识的资源
#  •  PUT 请求服务器存储一个资源,并用Request-URI作为
#  其标识
#  •  TRACE 请求服务器回送收到的请求信息,主要用于测试
#  或诊断
#  •  CONNECT 保留将来使用


#   GET请求
#   •  在浏览器的地址栏中输入网址的方式访问网页时,浏览器
#   采用GET方法,现在默认使用的协议版本是1.1
#   •  http
#   •  协议部分
#   : //
#   分隔符
#   模拟访问:
#   telnetlib.AOwww.tedu.cn80
#       
#       Trying60.10.3.93...
#       ConnectedDatagramProtocol(towww.tedu.cn.
#       EscapeSequence(characteris'^]'.
#   
#       GET/    HTTP/1.1
#       Host:   www.tedu.cn


#  GET请求(续1)
#  •  常用的请求报头
#  –  METHOD 请求资源的方法,这个是必须的
#  –  Host 被请求资源的名子,这个是必须的
#  –  Accept 请求报头域用于指定客户端接受哪些类型的信息
#  –  Accept-Encoding 它是用于指定可接受的内容编码
#  –  User-Agent 客户端信息
#  –  Connection 是否关闭连接GET应响消息
#  •  HTTP/1.1 200
#  协议、版本和状态码
#  •  Date 日期时间
#  •  Server 服务器信息
#  •  Content-Type 响应内容类型
#  •  Content-Length 响应数据长度
#  •  Last-Modified 资源最后更改时间
#  •  Connection
#  连接方式GET应响消息(续1)
#  HTTP/1.1200OK
#  Date:   Thu,    18Aug201610:15:04GMT
#  Server: tarena
#  Content-Type:   text/html
#  Content-Length: 159232
#  Accept-Ranges:  bytes(
#  Age:    3921
#  ConnecNon:  keep-alive
#      
#  <!DOCTYPEShtmlPUBLIC具体页面内容    POST方法
#  •  要求被请求服务器接受附在请求后面的数据
#  •  常用于提交表单
#  •  一般要在头部声明数据长度
#  •  信息头说明参见GET方法
