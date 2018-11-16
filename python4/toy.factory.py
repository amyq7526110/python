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

#  其他绑定方法
#  •  类中定义的方法需要绑定在具体的实例,由实例调用
#  •  实例方法需要明确调用


    def sing(self):
        print('I am %s, lalala'  % self.name)

if __name__ == '__main__':
    big = BearToy('雄大','Large','Brown')  # 将会调用__init__ 方法，big传递给self
    second = BearToy('雄王','Middle','Brown')
    print(big.size)
    print(big.color) 
    big.sing()
    second.sing()




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






