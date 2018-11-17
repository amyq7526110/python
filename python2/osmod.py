#!/usr/bin/env python3
import os
# os模块

# os模块简介
# •  对文件系统的访问大多通过python的os模块实现
# •  该模块是python访问操作系统功能的主要接口
# •  有些方法,如copy等,并没有提供,可以使用shutil
# 模块作为补充

# os模块方法

# symlink()  创建符号链接
# listdir()  列出指定目录的文件
# getcwd()   返回当前工作目录
# mkdir()    创建目录
# chmod()    改变权限模式
# getatime() 返回最近访问时间
# chdir()    改变工作目录
# remove()   删除文件

os.getcwd()                                # pwd
os.mkdir('/tmp/haha')                      # mkdir 
os.makedits('/tmp/haha/aaa/bbb')           # mkdir -p
os.listdir('/root/mei')                    # ls
os.chdir('/tmp/haha/')                     # cd
os.mknod('hello.txt')                      # touch
os.symlink('/etc/host','/tmp/haha/zhuji')  # ln -s
os.chmod('/tmp/haha',0o777)                # chmod 777 linux 8进制
os.system('ls -rl /tmp/haha')
os.path.split('/tmp/haha/hello.txt')
os.path.join('/tmp/haha','hello.txt')
os.path.isfile('/tmp/haha/hello.txt')      # -f
os.path.isdir('/tmp/haha')                 # -e
os.path.exists('/tmp/haha')                # -d
 





  
