#!/usr/bin/env python3
import re

def count_patt(fname,patt):
    patt_dict = {}
    cpatt  = re.compile(patt)
    with open(fname) as fobj:
         for line in fobj:
              m = cpatt.search(line)      
              if m:  
                  key = m.gropu()
                  patt_dict[key] = patt_dict.get(key, 0) +1
  
 

