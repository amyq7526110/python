#!/usr/bin/env python3

import os
import shutil

#  操作文件系统

os.chdir('/tmp')   
os.mkdir('example')
os.chdir('example')
os.mknod('test')
with open('test','w') as f:
    f.write('foo bar')
os.listdir('/tmp/example') 
with open('test') as f:
    print(f.read())
os.remove('test')
os.chdir('/tmp')
shutil.rmtree('example')



