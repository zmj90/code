"""
    自定义迭代器
    学习目的：
        1. 检验面向对象语法
        2. 深入了解迭代器框架
        3. 为生成器打下扎实基础
"""


class StudentIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __next__(self):
        if self.index == len(self.data) - 1:
            # 通过raise发送错误的对象
            raise StopIteration()
        self.index += 1
        # 通过return返回正确的结果
        return self.data[self.index]


class StudentController:
    def __init__(self):
        self.list_student = []

    def __iter__(self):
        return StudentIterator(self.list_student)


controller = StudentController()
controller.list_student.append("彭文韬")
controller.list_student.append("李佳辉")
controller.list_student.append("马振铭")
# for item in controller:
#     print(item)
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:  # 接收错误对象
        break
