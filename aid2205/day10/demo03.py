"""
    跨类调用
"""
# 需求：以面向对象思想,描述下列情景
# 情景：老张开车去东北
# 原则：类承担行为,对象存储数据

# 方式1:直接创建对象
# 语义:老张每次去东北都开新车
"""
class Person:
    def __init__(self,name):
        self.name = name

    def go_to(self): # 2
        print("去东北")
        car = Car()
        car.run()

class Car:
    def run(self): # 3
        print("行驶")

lz = Person("老张")
lz.go_to() # 1
"""

# 方式2:在构造函数中创建对象
# 语义:老张每次开自己的车去东北
"""
class Person:
    def __init__(self,name,xxx):
        self.name = name
        self.car = Car()

    def go_to(self): # 2
        print("去东北")
        print(self.name)
        self.car.run()

class Car:
    def run(self): # 3
        print("行驶")

lz = Person("老张")# 执行__init__
lz.go_to() # 1
"""

# 方式3:通过参数传递对象
# 语义:老张每次通过交通工具去东北
class Person:
    def __init__(self,name):
        self.name = name

    def go_to(self,vehicle): # 2
        print("去东北")
        print(self.name)
        vehicle.run()

class Car:
    def run(self): # 3
        print("行驶")

lz = Person("老张")
car = Car()
lz.go_to(car) # 1




# 面向过程
"""
def go_to(): # 2
    print("去东北")
    run()

def run(): # 3
    print("行驶")

go_to() # 1
"""