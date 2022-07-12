"""
    学生信息管理系统V1版本
        练习1:商品信息管理系统--添加信息
            View:显示菜单，选择菜单，录入信息
            model:商品名称,商品单价,商品编号
            controller:添加信息(方法体空白)
            调用view
        练习2:商品信息管理系统--存储信息，显示信息
            controller:存储信息(设置商品自增长编号,追加到列表)
            View:显示信息(输入2键,遍历controller列表)
        练习3:商品信息管理系统--删除信息
            View:删除信息(输入3键,获取编号显示成败)
            controller:移除信息(遍历列表查找,del元素)
        练习4:画出内存图，实现修改商品信息功能

"""


class StudentModel:
    """
        学生模型:将多个学生信息封装为一个Model类型
    """

    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        # 全球唯一标识符(由controller决定)
        self.sid = sid


class StudentView:
    """
        界面视图:负责处理学生信息的输入/输出逻辑
    """

    def __init__(self):
        self.controller = StudentController()

    def display_menu(self):
        """
            显示菜单
        """
        print("1键录入学生信息")
        print("2键显示学生信息")
        print("3键删除学生信息")
        print("4键修改学生信息")

    def select_menu(self):
        """
            选择菜单
        """
        item = input("请输入选项:")
        if item == "1":
            # 难点1:本类多个方法互相调用
            # 通过self调用
            self.input_student()
        elif item == "2":
            self.display_students()
        elif item == "3":
            self.delete_student()
        elif item == "4":
            self.modify_student()

    def input_student(self):
        """
            录入学生信息
        """
        # 难点2:跨类调用方式1(直接创建对象)
        model = StudentModel()
        model.name = input("请输入学生姓名:")
        model.age = int(input("请输入学生年龄:"))
        model.score = int(input("请输入学生成绩:"))
        self.controller.add_student(model)
        print("添加成功")

    def display_students(self):
        for item in self.controller.list_student:
            print(f"{item.name}的编号是{item.sid},年龄是{item.age},成绩是{item.score}")

    def delete_student(self):
        sid = int(input("请输入需要删除的编号："))
        if self.controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def modify_student(self):
        model = StudentModel()
        model.sid = int(input("请输入学生编号:"))
        model.name = input("请输入学生姓名:")
        model.age = int(input("请输入学生年龄:"))
        model.score = int(input("请输入学生成绩:"))
        if self.controller.update_student(model):
            print("修改成功")
        else:
            print("修改失败")


class StudentController:
    def __init__(self):
        self.start_id = 1001
        self.list_student = []

    def add_student(self, new):
        """
            添加学生信息(设置学生编号,追加到列表中)
        :param new: StudentModel类型,在view中录入的学生信息
        """
        # 自增长
        new.sid = self.start_id
        self.start_id += 1
        self.list_student.append(new)

    def remove_student(self, sid):
        """
            在列表中移除学生信息
        :param sid: 学生编号
        :return: 是否移除成功
        """
        for i in range(len(self.list_student)):
            if self.list_student[i].sid == sid:
                del self.list_student[i]
                return True
        return False

    def update_student(self, model):
        """
            修改学生信息
        :param model: StudentModel类型,需要修改的信息
        :return: bool类型,是否修改成功
        """
        # for i in range(len(self.list_student)):
        #     if self.list_student[i].sid == model.sid:
        #         # self.list_student[i].name = model.name
        #         # self.list_student[i].age = model.age
        #         # self.list_student[i].score = model.score
        #         self.list_student[i].__dict__ = model.__dict__
        #         return True
        # return False
        for item in self.list_student:
            if item.sid == model.sid:
                item.__dict__ = model.__dict__
                return True
        return False


view = StudentView()
while True:
    view.display_menu()
    view.select_menu()
