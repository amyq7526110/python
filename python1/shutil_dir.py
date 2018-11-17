#!/usr/bin/env python3

import shutil
import os

#  目录操作
#  •  shutil.copytree(src, dst, symlinks=False, ignore=
#  None, copy_function=copy2, ignore_dangling_s
#  ymlinks=False)
#  递归地复制以src为根的整个目录树,返回目标目录。由
#  dst命名的目标目录不能已经存在。

#  shutil.copytree('/tmp/tesss','/opt/tesss/')
#  os.system('ls /opt/ -l')


#  •  shutil.rmtree (path, ignore_errors=False, onerror=None)
#  删除整个目录树; 路径必须指向目录(而不是指向目录
#  的符号链接)。
#  shutil.rmtree('/opt/tesss')
#  os.system('ls /opt/ -l')


#   权限管理
#   •  shutil.copymode(src, dst, *, follow_symlinks=True)
#   将权限位从src复制到dst。文件内容,所有者和组不受影
#   响。src和dst是以字符串形式给出的路径名称。
#   os.system('ls -l /etc/shadow')
#   os.system('ls -l /tmp/mima2.txt')
#   shutil.copymode('/etc/shadow','/tmp/mima2.txt')
os.system('ls -l /tmp/mima2.txt')

#
#   shutil.copystat(src, dst, *, follow_symlinks=True)
#   将权限位,最后访问时间,上次修改时间和标志从src
#   复制到dst。
#   os.system('stat /etc/shadow')
#   shutil.copystat('/etc/shadow' ,'/tmp/mima2.txt')
#   os.system('stat /tmp/mima2.txt')

#   •  shutil.chown(path, user=None, group=None)
#      更改给定路径的所有者用户和/或组


#  shutil.chown('/tmp/mima2.txt',user='Student',group='apache')
#  os.system('ls -l /tmp/mima2.txt')

with open('/etc/passwd','rb') as src_obj:
     with open('/tmp/mtem.txt') as dest_obj:
          shutil.copyfileobj(src_obj,dest_obj)










