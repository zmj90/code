"""
    继承
        财产：钱不用孩子挣,但是可以直接花
        编程：代码不用子类写,但是可以直接用
"""
# 适用性
# 多个类型,代码有共性,在概念上又统一
"""
class Student:
    def play(self):
        print("在玩耍")
    
    def say(self):
        print("在说话")

class Teacher:
    def teach(self):
        print("在讲课")
    
    def say(self):
        print("在说话")
"""


# 按编码(执行)顺序：先有父类,再有子类
# 按设计思想顺序：先有子类,再有父类
class Person:
    def say(self):
        print("在说话")

class Student(Person):
    def play(self):
        print("在玩耍")
        self.say()

class Teacher(Person):
    def teach(self):
        print("在讲课")

# 创建子类对象,可以访问父类与子类成员
t = Teacher()
t.say()
t.teach() # teach(t)

# 创建父类对象,只能访问父类
p = Person()
p.say()

# 关系判定
# isinstance(对象,类型)
# 老师对象 是一种 人类型
print(isinstance(t, Person))  # True
# 老师对象 是一种 老师类型
print(isinstance(t, Teacher))  # True
# 人对象 是一种 老师类型
print(isinstance(p, Teacher))  # False

# issubclass(类型,类型)
# 老师类型 是一种 人类型
print(issubclass(Teacher, Person))  # True
# 老师类型 是一种 老师类型
print(issubclass(Teacher, Teacher))  # True
# 人类型 是一种 老师类型
print(issubclass(Person, Teacher))  # False

# type(对象) == 类型
# 老师对象的类型 是 人类型
print(type(t) == Person)  # False
# 老师对象的类型 是 老师类型
print(type(t) == Teacher)  # True
# 人对象的类型 是 老师类型
print(type(p) == Teacher)  # False
