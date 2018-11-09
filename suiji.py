#!/usr/bin/env python3
import os
import readline
import subprocess
import random
number = random.randint(1,10)
print (number)
os.system('ls')
a=os.popen('echo $[RANDOM%3]').readline()
print(a)
subprocess.call(["ls","-l"])

