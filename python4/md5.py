#!/usr/bin/env python3

import hashlib
import sys

with open('/etc/passwd','rb') as fobi:
       date = fobi.read()

m = hashlib.md5(date)

print(m.hexdigest())  # 8093312542f8308ac670bc425b2aad86

b = hashlib.sha512(date)

print(b.hexdigest())  # d7f6ab5a7a23e5e8aac5783dcca7b98d694952d814da064a6013d2c213a550986c4750aac4742386375e81bed5ef7780dc6a688e53f5be982e67e3d34e2c604a


#  上面的方法不具有通用性

#  使用下面的好

def md5file(fname):
    a = hashlib.md5()
    with open(fname,'rb') as fobj:
        while True: 
            data = fobj.read(4096)
            if not data:  
                break 
            a.update(data)
    return a.hexdigest() 
if __name__ == '__main__':
    print(md5file('/etc/passwd'))  # 8093312542f8308ac670bc425b2aad86
    print(md5file(sys.argv[1]))
          

