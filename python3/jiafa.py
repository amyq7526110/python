#!/usr/bin/env python3


from random import randint
def add(x,y):
    return  x + y
def sub(x,y):
    return  x - y
def exam():
    a = [randint(1,100),randint(1,100)]
    if a[0] < a[1]:
        a[0],a[1] = a[1],a[0]
        print('%s - %s = ' % (a[0],a[1]),end='')
        result = a[0] - a[1]
    else:
        print('%s + %s = ' % (a[0],a[1]),end='')
        result = a[0]  + a[1]
    answer = int(input())
    count = 0
    while  count < 3:
        if result == answer:
            print('Vrey Good!!')
            break
        count += 1
    else:
         print('你的机会用完了')
def main():
    while True:
        exam()
        answer = input('Continue？(y/n)').strip()[0]
        if answer in ['n','N']:
            break
if __name__ == '__main__':
    main()
        
 


