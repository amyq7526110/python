#!/usr/bin/env python3

class A:
    def foo(self):
        print('你好')
    def pstar(self):
        print('#' * 20)
class B:
    def bar(self):
        print('How are you')
    def pstar(self):
        print('$' * 20)
#class C(A,B):
class C(B,A):
   pass
#    def pstar(self):
#        print('*' * 20)

if __name__ == '__main__': 
    c = C()   # 
    c.foo()
    c.bar()
    c.pstar()
   
#  通过继承覆盖方法
#  •  如果子类中有和父类同名的方法,父类方法将被覆盖
#  •  如果需要访问父类的方法,则要调用一个未绑定的父
#  类方法,明确给出子类的实例
 
#  多重继承
#  •  python允许多重继承,即一个类可以是多个父类的
#  子类,子类可以拥有所有父类的属性 
