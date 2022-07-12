"""
    数据继承
"""


class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

# 子类没有构造函数,使用继承而来的父类构造函数
class Student(Person):
    pass

# 1.子类有构造函数,覆盖父类构造函数(不执行)
# 2.此时必须通过super函数调用父类构造函数
# 3.子类构造函数参数：父参数+子参数
class Teacher(Person):
    def __init__(self, name="", age=0, salary=0):
        super().__init__(name, age)
        self.salary = salary

p = Person("彭文韬", 23)
s = Student("彭文韬", 23)
t = Teacher("祁大圣", 18, 100000)
print(s.__dict__)
print(t.__dict__)
