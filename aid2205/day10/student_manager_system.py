"""
    餐厅架构:
        迎宾 -> 服务员 -> 厨师 -> 传菜员 -> 收银员

    软件架构:
        视图View            控制器Controller
       (界面逻辑)              (业务逻辑)
                数据模型Model
               (将多个数据封装一个)
    练习:商品信息管理系统--添加信息
        View:显示菜单，选择菜单，录入信息
        model:商品名称,商品单价,商品编号
        controller:添加信息(方法体空白)
        调用view
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

class StudentController:
    def add_student(self, new):
        """
            添加学生信息(设置学生编号,追加到列表中)
        :param new: StudentModel类型,在view中录入的学生信息
        """
        pass

view = StudentView()
while True:
    view.display_menu()
    view.select_menu()
