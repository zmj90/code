"""
    封装[分]：分而治之，变则疏之
            例如：创建人类、汽车、飞机..
    继承[隔]：统一行为，隔离变化
            例如：创建交通工具统一汽车、飞机的运输方法
                交通工具隔离了人类和汽车、飞机
    多态[做]：编码时调用父，运行时执行子
            例如：人类调用交通工具方法
                 汽车、飞机重写交通工具方法
"""
# 需求:老张开车去东北
# 变化：增加飞机
"""
class Person:
    def __init__(self,name):
        self.name = name

    def go_to(self,vehicle): # 2
        print("去东北")
        # 违背了开闭原则
        if type(vehicle) == Car:
            vehicle.run()
        elif type(vehicle) == Airplane:
            vehicle.fly()

class Car:
    def run(self): # 3
        print("行驶")

class Airplane:
    def fly(self):
        print("飞行")

lz = Person("老张")
car = Car()
lz.go_to(car) # 1
air = Airplane()
lz.go_to(air) # 1
"""


# ----------------架构师-----------------------

class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle):
        # 传入的对象是一种交通工具(对象就有transport方法)
        if isinstance(vehicle, Vehicle):
            print("去东北")
            # 在客户端代码中：
            # 编码时,调用父类方法
            # 运行时,执行子类方法
            vehicle.transport()

# 父类
class Vehicle:
    """
        交通工具
    """
    def transport(self):
        pass

# -----------------程序员----------------------...10年...
class Car(Vehicle):
    def transport(self):
        print("汽车在行驶")

class Airplane(Vehicle):
    def transport(self):
        print("飞机在飞行")


# ------------------测试---------------------
p = Person("老张")
p.go_to(Car())
p.go_to(Airplane())
p.go_to("轮船")
