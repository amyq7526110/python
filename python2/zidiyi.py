#!/usr/bin/env python3

#  自定义异常


def set_im(name,age):
    if not   0 < age < 150:
        raise ValueError('age is too great')
    print('%s is %d years old' % (name,age)) 
def set_im2(name,age):
    assert 0 < age < 150 , ' age out of range '
    print('%s is %d years old' % (name,age)) 
if __name__ == '__main__':
   set_im('bob',23)
   set_im2('bob',223)
