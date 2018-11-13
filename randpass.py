#!/usr/bin/env python3
from  random import choice
from  string import ascii_letters,digits
import sys
def rapass():
#    lst =  ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lst = ascii_letters+digits+'_.'
    passed = choice(lst)
    for i in range(int(sys.argv[1])-1):
        passed =  passed + choice(lst)
    print(passed)
if __name__ == '__main__':
    rapass()

 
     
