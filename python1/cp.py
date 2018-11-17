#!/usr/bin/env python3
import sys
def cp_file():
    print(sys.argv)
    src_obj = open(sys.argv[1],'rb')
    dest_obj = open(sys.argv[2],'wb')
    while True:
        data = src_obj.read(4096)
        if  not data:
            break
        dest_obj.write(data)
    src_obj.close()
    dest_obj.close()
     
cp_file()










