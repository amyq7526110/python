#!/usr/bin/env python3
with open('test') as fobj:
    aset = set(fobj)
with open('test.txt') as fobj:
    bset = set(fobj)
with open('newfile.txt','w') as fobj:
    fobj.writelines(aset - bset)

