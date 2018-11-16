#!/usr/bin/env python3

# tarfile
  
# •  tarfile模块允许创建、访问tar文件

# •  同时支持gzip、bzip2格式

import os 

import tarfile


tar = tarfile.open('/tmp/security.tar.gz','w:gz')
os.chdir('/etc')
tar.add('security')
tar.add('hosts')
tar.close()

os.mkdir('/tmp/anquan')
os.chdir('/tmp/anquan')
tar = tarfile.open('/tmp/security.tar.gz','r:gz')
tar.extractall()
tar.close()





