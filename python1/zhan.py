#!/usr/bin/env  python3
def ruzhan(c):
    item = input('please input ruzhan content ').strip()
    if item:
        c.append(item)
def chuzhan(c):
    x  =   input('please input you want pop number ')
    if not  x.isdigit():
        print('\033[31m please input a number \033[0m')
    else:
        if  len(c) < int(x):
            print("\033[31m don't have x de content \033[0m")
        else:	
            for i in range(0,int(x)):
                print('\033[36m %s \033[0m' % c.pop())
def chazhan(c):
    print('\033[32m %s \033[0m' % c)
def zhanmian(c):
    cmds = {'1':chazhan,'2':ruzhan,'3':chuzhan}
    potal = '''
1 查询
2 入栈
3 出栈
q quit
please input your chioce : 
'''
    while True:
        chioce  =  input(potal).strip()[0]
    
        if chioce not in '123q':
            continue
        elif chioce == 'q':  
            break
        cmds[chioce](c)
    #    elif chioce == '1':
    #        chazhan(c)
    #    elif chioce == '2':
    #        ruzhan(c)
    #    elif chioce == '3': 	
    #        chuzhan(c)
if __name__ == '__main__':
    c = []
    zhanmian(c)
     
