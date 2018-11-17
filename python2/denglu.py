#!/usr/bin/env python3
import getpass
import re
users = {}
def denglu():
    username = input('please input your username: ').strip()
    password = getpass.getpass('password: ')
#    if username in users and password == users.get(username):
    if users.get(username) == password:
        print('\033[32m Login successful \033[0m')
    else:	
        print('\033[31m Login failed \033[0m')
def zhuce():
    username = input('please input your sign up username: ').strip()
    password = getpass.getpass('password: ')
    if username in users:
        print('\033[31m %s is exist ! \033\0m' % username )
    else:
        if username and password: 
            users[username] = password 
            print('\033[32mSign up successful\033[0m ') 
        else:
            print('\033[31m Sign up falied \033[0m')
def dlmenu():
    cmds = {'_1':denglu,'_2':zhuce}    
    potal = '''\033[36m1 登陆
2 注册
q 退出
please input your choice : \033[0m'''
    while True:
        choice = '_'+input(potal).strip()
#        if  re.match(r'^_[^12q]',choice):
#            continue 
        if  not re.match(r'^_[12q]$',choice):
            print('\033[31m Invalid choice, Try again\033[0m')
            continue 
#        if choice  ==  '_':
#            continue
        elif choice == '_q':
            break
        cmds[choice]()
if __name__ == '__main__': 
    dlmenu()
    
