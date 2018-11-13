#!/usr/bin/env python3
from createfile import get_content
#  字符串

#  字符串操作符

#    比较操作符:字符串大小按ASCII码值大小进行比较
#    切片操作符:[ ]、[ : ]、[ : : ]
#    成员关系操作符:in、not in

#  格式化操作符

#  字符串可以使用格式化符号来表示特定含义

#  格式化字符     转换方式
#  %c             转换成字符
#  %s             优先用str()函数进行字符串转换
#  %d / %i        转成有符号十进制数
#  %o             转成无符号八进制数
#  %e / %E        转成科学计数法
#  %f / %F        转成浮点数

print('%d/%d/%d %d:%d' % (2018,11,12,15,22))
print('username = %s \npassword = %s ' % ( 'haha',123456))

#  注意： 运行格式化字符串时，将参数按照顺序传入格式符

#  格式化操作符(续1)

#    字符串可以使用格式化符号来表示特定含义

#    辅助指令       作用

#    *              定义宽度或者小数点精度
#    -              左对齐
#    +              在正数前面显示加号
#    <sp>           在正数前面显示空格
#    #              在八进制数前面显示零0,在十六进制前面显
#                   示'0x'或者'0X'
#    0              显示的数字前面填充0而不是默认的空格



print( '%d'  % 20)
print( '%+8d'% 20)
print( '%o'  % 20)
print( '%#d' % 20)
print( '%8f' % 20)
print( '% 8d'  % 20)


#  format函数

#    使用位置参数
print('my name is {} ,age  is {}'.format('hoho',18))

#    使用关键字参数

print('my name is {name} ,age is {age}'.format(name='bob',age=18))
a = {'name':'lele','age':10}
print(a)
# print('my name is {name} ,age is  {age}'.format(a))

#    填充与格式化

#    {:[填充字符][对齐方式 <^>][宽度]}

#    默认空格填充

print('{:_^50}'.format("hello world"))
print('{:_<50}'.format("hello world"))
print('{:_>50}'.format("hello world"))

#    使用索引
print('name is {0[0]} age is {0[1]}'.format(['bob', 23]))

def gecontent(content):
    print('+'+'*' * 48+'+')
    for i in content:
        print('+{:^48}+'.format(i))
    print('+'+'*' * 48+ '+')


if __name__ == '__main__':
    a = get_content()
    gecontent(a)    


#  原始字符串操作符

#      原始字符串操作符是为了对付那些在字符串中出现的特殊字符

#      在原始字符串里,所有的字符都是直接按照字面的意
#   思来使用,没有转义特殊或不能打印的字符,

winPath = "c:\windows\temp"
print(winPath)
# c:\windows    emp

newPath = r"c:\windows\temp"
print(newPath)
# c:\windows\temp
