#!/usr/bin/env python3
import os
import time

pid = os.fork()

if pid:
   print('parent.....')
   time.sleep(20)
else:
   print('child......')
   time.sleep(15)


