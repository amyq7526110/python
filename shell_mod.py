#!/usr/bin/env python3

import shutil  #  shutil模块 提供对文件的 复制和移动操作
import os

#  •  shutil.copyfileobj(fsrc, fdst[, length])

#  将类似文件的对象fsrc的内容复制到类似文件的对象fdst。

#  •  shutil.copyfile(src, dst, *, follow_symlinks=True)

#  将名为src的文件的内容(无元数据)复制到名为dst的文
#  件,然后返回dst。
#  shutil.copyfileobj(open('/etc/passwd','rb'),open('/tmp/mima','wb'))

#  shutil.copyfile('/etc/passwd','/tmp/mima2.txt')

# os.system('ls /tmp/mima* -l')


#  •  shutil.copy(src, dst, *, follow_symlinks=True)
#  将文件src复制到文件或目录dst。src和dst应为字符
#  串。如果dst指定目录,则文件将使用src的基本文件
#  名复制到dst中。返回新创建的文件的路径。
shutil.copy('/etc/shadow','/tmp')
os.system('ls /tmp/sh* -l') 

# •  shutil.copy2(src, dst, *, follow_symlinks=True)
# 与copy()相同,但copy2()也尝试保留所有文件元数据。

shutil.copy2('haha','/tmp')
os.system(' ls  /tmp/haha -l')


#  shutil.move(src, dst, copy_function=copy2)
#  $递归地将文件或目录(src)移动到另一个位置
#  (dst),并返回目标。
#  
#  shutil.move('/root/tesss','/tmp')
#  os.system('ls /tmp/tesss -ld')


















