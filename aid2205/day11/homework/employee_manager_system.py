"""
    员工信息管理系统
"""


class EmployeesModel:
    """
        员工数据模型
    """

    def __init__(self, eid=0, did=0, name="", money=0):
        self.eid = eid  # 全球唯一标识符
        self.did = did
        self.name = name
        self.money = money


class EmployeesView:
    """
        员工视图
    """

    def __init__(self):
        self.controller = EmployeesController()

    def display_menu(self):
        print("1键添加员工信息")
        print("2键显示员工信息")
        print("3键删除员工信息")
        print("4键修改员工信息")

    def select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.input_employees()

    def input_employees(self):
        model = EmployeesModel()
        model.did = int(input("请输入部门编号："))
        model.name = input("请输入员工姓名：")
        model.money = int(input("请输入员工工资："))
        self.controller.add_employees(model)
        print("添加成功")


class EmployeesController:
    """
        员工控制器
    """

    def add_employees(self, new):
        pass


view = EmployeesView()  # controller  list
while True:
    view.display_menu()
    view.select_menu()
