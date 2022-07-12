"""
    迭代器-->yield
"""


class StudentController:
    def __init__(self):
        self.list_student = []

    def __iter__(self):
        # 自动生成迭代器代码大致规则：
        # 1. 将yield关键字之前的代码定义在__next__函数中
        # 2. 将yield关键字之后的代码作为__next__函数返回值
        index = 0
        yield self.list_student[index]
        index += 1
        yield self.list_student[index]
        index += 1
        yield self.list_student[index]


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
