#!/usr/bin/env python3

#    九九乘法表

x = int(input('请输入一个数字' ))  
for i in range(1,x+1):    
    for j in range(1,i+1):
#        print(j,'x',i,'=',i*j,sep='',end=' ')  
#        print(str(i)+'x'+str(j)+'='+str(j*i),end=' ')
        print('%dx%d=%d'% (i,j,i*j),end=' ')
    print()
print()

   
