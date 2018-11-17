#!/usr/bin/env python3
import  sys
def unix2doc(fname,end='\r\n'):
    new_fname = fname+'.txt'
    with open(fname) as wf:
        with  open(new_fname,'w') as nf:
            for line in wf: 
                nf.write(line.rstrip() + end )
if __name__ == '__main__':
    unix2doc(sys.argv[1])
