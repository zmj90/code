"""
    学生信息管理系统V6版本
"""
from dal import StudentDao
from model import StudentModel


class StudentView:
    """
        界面视图:负责处理学生信息的输入/输出逻辑
    """

    def __init__(self):
        self.__controller = StudentController()

    def __display_menu(self):
        """
            显示菜单
        """
        print("1键录入学生信息")
        print("2键显示学生信息")
        print("3键删除学生信息")
        print("4键修改学生信息")

    def __select_menu(self):
        """
            选择菜单
        """
        item = input("请输入选项:")
        if item == "1":
            # 难点1:本类多个方法互相调用
            # 通过self调用
            self.__input_student()
        elif item == "2":
            self.__display_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()

    def __input_student(self):
        """
            录入学生信息
        """
        # 难点2:跨类调用方式1(直接创建对象)
        model = StudentModel()
        model.name = input("请输入学生姓名:")
        model.age = int(input("请输入学生年龄:"))
        model.score = int(input("请输入学生成绩:"))
        self.__controller.add_student(model)
        print("添加成功")

    def __display_students(self):
        for item in self.__controller.list_student:
            # print(f"{item.name}的编号是{item.sid},年龄是{item.age},成绩是{item.score}")
            # 此时需要重写model类的__str__
            print(item)  # 打印自定义对象,自动执行__str__

    def __delete_student(self):
        sid = int(input("请输入需要删除的编号："))
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        model = StudentModel()
        model.sid = int(input("请输入学生编号:"))
        model.name = input("请输入学生姓名:")
        model.age = int(input("请输入学生年龄:"))
        model.score = int(input("请输入学生成绩:"))
        if self.__controller.update_student(model):
            print("修改成功")
        else:
            print("修改失败")

    def main(self):
        """
            入口
        """
        while True:
            self.__display_menu()
            self.__select_menu()


class StudentController:
    def __init__(self):
        self.__start_id = 1001
        self.dao = StudentDao()
        self.list_student = self.dao.load() # 必须存在文件

    def add_student(self, new):
        """
            添加学生信息(设置学生编号,追加到列表中)
        :param new: StudentModel类型,在view中录入的学生信息
        """
        # 自增长
        new.sid = self.__start_id
        self.__start_id += 1
        self.list_student.append(new)
        self.dao.save(self.list_student)

    def remove_student(self, sid):
        """
            在列表中移除学生信息
        :param sid: 学生编号
        :return: 是否移除成功
        """
        if sid in self.list_student:
            self.list_student.remove(sid)
            self.dao.save(self.list_student)
            return True
        return False
        # remove内部代码：
        # for i in range(len(self.list_student)):
        #     if self.list_student[i] == sid:
        #     if self.list_student[i].__eq__(sid):
        #     重写model的__eq__
        #     if self.list_student[i].sid == sid:
        #         del self.list_student[i]
        #         break

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
                self.dao.save(self.list_student)
                return True
        return False


view = StudentView()
view.main()
