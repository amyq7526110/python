#!/usr/bin/env python3
import os
import time
for i in range(3):
    pid  = os.fork()
    if not pid:
       print('Hello world')
       exit()
time.sleep(0.01)
print('\033[32mDone\033[0m')
