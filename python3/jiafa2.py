#!/usr/bin/env python3
import random
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def exam():
    cmds = {'+':add,'-':sub}
    a = [ random.randint(1,100) for i in range(2) ]
    a.sort(reverse=True)
    op = random.choice('+-')
    result = cmds[op](*a)
    prompt = '%s %s %s = ' % (a[0],op,a[1])
    count = 0
    while count < 3:
        try:
            answer = int(input(prompt))
        except:
            continue
        if result == answer:
            print('Vrey Good!!')
            break
        print('Your answ Wrong')
        count += 1
    else:
        print('你的机会用完了,正确的答案 %s' % result)
def main():
    while True:
        exam()
        try:
            answer = input('Continue？(y/n)').strip()[0]
        except (IndentationError,ValueError):
            continue
        except (KeyboardInterrupt,EOFError):
            answer = 'n'
            print()
        if answer in ['n', 'N']:
            break
if __name__ == '__main__':
    main()
