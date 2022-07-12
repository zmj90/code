"""
    私有化
        语法：以双下划线命名
        原理：自动将私有变量名改为:单下划线+类名+私有变量名
            例如：__age --> _Person__age
"""


class Person:
    def __init__(self, name=""):
        self.name = name
        self.__age = 18

    def say(self):
        # 类内可以访问,私有成员
        print(self.__age)


wlh = Person("王利花")
# 类外无法访问,私有成员
# print(wlh.__age)
wlh.say()
print(wlh.__dict__)
