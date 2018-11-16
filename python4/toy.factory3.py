#!/usr/bin/env python3

#  构造器方法
#  •  当实例化类的对象是,构造器方法默认自动调用
#  •  实例本身作为第一个参数,传递给self

class BearToy:
    def __init__(self,name,size,color):
         "实例化自动调用"
         self.name = name    # 绑定属性到self 上整个类可以引用
         self.size = size
         self.color = color

#  创建子类(续1)
#•      创建子类只需要在圆括号中写明从哪个父类继承即可

class NewBear(BearToy):  # 
    def run(self):
        print('我能爬！')

#     创建子类
#     •  当类之间有显著的不同,并且较小的类是较大的类所
#     需要的组件时组合表现得很好;但当设计“相同的类
#     但有一些不同的功能”时,派生就是一个更加合理的
#     选择了
#     •  OOP 的更强大方面之一是能够使用一个已经定义好
#     的类,扩展它或者对其进行修改,而不会影响系统中
#     使用现存类的其它代码片段
#     •  OOD(面向对象设计)允许类特征在子孙类或子类中进行继承

#  其他绑定方法
#  •  类中定义的方法需要绑定在具体的实例,由实例调用
#  •  实例方法需要明确调用


    def sing(self):
        print('I am %s, lalala'  % self.name)

if __name__ == '__main__':
    big = NewBear('雄大','Large','Brown')  # 将会调用__init__ 方法，big传递给self
    big.run()
    print(big.name)



#  组合应用
#  •  两个类明显不同
#  •  一个类是另一个类的组件
#  知
#  识
#  讲
#  解
#  classManufacture: 
#      def__init__(self, phone, email): 
#          self.phone= phone2numeric(
#          self.email= email
#   
#  classBearToy: 
#      def__init__(self, size, color, phone, email): 
#          self.size= sizeCentralDir
#          self.color= color_content(
#          self.vendor= Manufacture(phone, email) 






