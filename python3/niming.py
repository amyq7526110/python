#!/usr/bin/env python3
import random
#def exam():
#    cmds = {'+':lambda x,y : x+y,'-': lambda x,y:x-y}
#    a = [ random.randint(1,100) for i in range(2) ]
#    a.sort(reverse=True)
#    op = random.choice('+-')
#    result = cmds[op](*a)
#    prompt = '%s %s %s = ' % (a[0],op,a[1])
#    count = 0
#    while count < 3:
#        try:
#            answer = int(input(prompt))
#        except:
#            continue
#        if result == answer:
#            print('Vrey Good!!')
#            break
#        print('Your answ Wrong')
#        count += 1
#    else:
#        print('你的机会用完了,正确的答案 %s' % result)
#def main():
#    while True:
#        exam()
#        try:
#            answer = input('Continue？(y/n)').strip()[0]
#        except (IndentationError,ValueError):
#            continue
#        except (KeyboardInterrupt,EOFError):
#            answer = 'n'
#            print()
#        if answer in ['n', 'N']:
#            break
#if __name__ == '__main__':
#    main()
#  匿名函数


#  lambda
#  •  python允许用lambda关键字创造匿名函数
#  •  匿名是因为不需要以标准的def方式来声明
#  •  一个完整的lambda“语句”代表了一个表达式,这
#  个表达式的定义体必须和声明放在同一行

def add(x,y):
    return x + y
a = lambda x,y: x + y
print(add(10,20))           #  30 
print(a(10,20))             #  30


#   filter()函数
#   •  filter(func, seq):调用一个布尔函数func来迭代遍历
#   每个序列中的元素;返回一个使func返回值为true的
#   元素的序列
#   •  如果布尔函数比较简单,直接使用lambda匿名函数
#   就显得非常方便了

def func1(x):
    return x % 2 

nums = [random.randint(1,100) for i in range(10) ]
print(nums)
print(list(filter(func1,nums)))
print(list(filter(lambda x: x % 2,nums)))      


#   map()函数 调用函数对后面的值进行处理

def func2(x):
    return x * 2 +1
print(list(map(func2,nums)))   
print(list(map(lambda x: x * 2 + 1,nums)))
















