#!/usr/bin/env python3

import pickle as p

# pickle模块简介

# •  把数据写入文件时,常规的文件方法只能把字符串对
# 象写入。其他数据需先转换成字符串再写入文件 。
# •  python提供了一个标准的模块,称为pickle。使用它
# 可以在一个文件中储存任何python对象,之后又可
# 以把它完整无缺地取出来

# pickle模块方法
# •  分别调用dump()和load()可以存储、写入
a = {'name':'bob','age':16}
with open('/tmp/adc.data','wb') as wf:
    p.dump(a,wf)
with open('/tmp/adc.data','rb') as wf:
    a = p.load(wf)
print(a)


