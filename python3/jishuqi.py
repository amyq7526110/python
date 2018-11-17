#!/usr/bin/env python3

#  计数器

def counter(start=0):
    count = start
    def incr():
        nonlocal count
        count += 1
        return count  
    return incr
a = counter()
b = counter(10)

print(a())
print(b())
