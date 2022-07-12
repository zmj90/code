"""
    重写
        子类具有和父类名称相同的方法
        作用：改变父类行为
"""


# "结论"：如果希望指定打印自定义对象的格式
#       需要重写自定义类的__str__方法
class Person(object):
    # 魔法方法:在特定时机自动执行的方法
    # 创建对象时自动执行
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 打印自定义对象时自动执行
    def __str__(self):
        # object类的写法
        # return "<__main__.Person object at 0x7ff7e29fc7c0>"
        return f"{self.name}的年龄是{self.age}"

    # 自定义对象转换为int类型时自动执行
    def __int__(self):
        return self.age


p = Person("彭文韬", 23)
# 默认：<__main__.Person object at 0x7ff7e29fc7c0>
print(p)  # print内部：执行p的__str__方法

print(int(p))
