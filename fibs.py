#!/usr/bin/env python3
def fib(x):
    fibo = [0,1 ]
    for i in range(x-2):
        fibo.append(fibo[-1]+fibo[-2])
    print(fibo)
#fibs(10)
#febo(6)
#febo(10)
print(__name__)  # 保存模块名

# 当模块直接执行是__name__的值为__name__

#
if __name__  == '__mian__':
    fib(10)









