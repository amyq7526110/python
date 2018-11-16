#!/usr/bin/env python3


class Book:

    def __init__(self,title,auther):
         self.title = title
         self.auther = auther

    def __str__(self):
         return "<%s>" % self.title

    def __call__(self):
         print('<%s> 是 %s 写的' % (self.title,self.auther))

if __name__ == '__main__':
    core_py = Book('Python核心编程','wesley')
    print(core_py)
    core_py()


