#!/usr/bin/env python3

import tarfile 
import hashlib
import os
import sys
import pickle  as p 
import time

md5zhi = {}

def md5file(fname):
    a = hashlib.md5()
    with open(fname,'rb') as fobj:
        while True: 
            data = fobj.read(4096)
            if not data:  
                break 
            a.update(data)
    return a.hexdigest() 

def file_name(file_dir):
    for root,dirs,files in os.walk(file_dir):
        x =  [ root+'/'+i  for i in files  ]
        for i in x: 
            a = md5file(i)        
            md5zhi[i] =  a
    return md5zhi
def beifei(file_dir):
    record = '/var/log/backup/'+  time.strftime('%Y-%U',time.localtime()) + '.data'
    tarname = '/tmp/backup/'  + time.strftime('%Y-%m-%d-%M',time.localtime()) +'.tar.gz'
    if not os.path.exists(record):
        mf5info = file_name(file_dir)
        with open(record,'wb') as wf:
             p.dump(mf5info,wf)
        tar = tarfile.open(tarname,'w:gz')
        tar.add(file_dir)             
        tar.close
    else:
        with open(record,'rb') as wf:
             a = p.load(wf)
        b = file_name(file_dir)
        tar = tarfile.open(tarname,'w:gz')
        for i in b:
            if i not in a:
                tar.add(i)
            else:
                if  b[i] != a[i]:
                    tar.add(i)
        tar.close()
        with open(record,'wb') as wf:
             p.dump(b,wf)
if __name__ == '__main__': 
    beifei('/root/tees')
