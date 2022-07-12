"""
    创建狗类
    数据：
        品种、昵称、身长、体重
    行为：
        吃(体重增长1)
    实例化两个对象并调用其函数
    画出内存图
"""


# 对象.成员名
# 类中self就是对象
# 类外自定义对象名就是对象

class Dog:
    def __init__(self, species="", pet_name="", height=0.0, weight=0):
        self.species = species
        self.pet_name = pet_name
        self.height = height
        self.weight = weight

    def eat(self):
        self.weight += 1
        print("吃饭饭~")


mi_xiu = Dog("拉布拉多", "米咻", 0.6, 60)
mi_xiu.eat()
print(mi_xiu.weight)

hei_mi = Dog("拉布拉多", "黑米", 0.5, 50)
hei_mi.eat()
print(hei_mi.weight)
