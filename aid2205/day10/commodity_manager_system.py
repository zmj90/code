"""
    练习:商品信息管理系统
"""


class CommodityModel:
    """
        商品模型:将多个商品信息封装为一个Model类型
    """

    def __init__(self, name="", price=0, cid=0):
        self.name = name
        self.price = price
        # 全球唯一标识符(由controller决定)
        self.cid = cid


class CommodityView:
    """
        界面视图:负责处理商品信息的输入/输出逻辑
    """

    def __init__(self):
        self.controller = CommodityController()

    def display_menu(self):
        """
            显示菜单
        """
        print("1键录入商品信息")
        print("2键显示商品信息")
        print("3键删除商品信息")
        print("4键修改商品信息")

    def select_menu(self):
        """
            选择菜单
        """
        item = input("请输入选项:")
        if item == "1":
            # 难点1:本类多个方法互相调用
            # 通过self调用
            self.input_commodity()

    def input_commodity(self):
        """
            录入商品信息
        """
        # 难点2:跨类调用方式1(直接创建对象)
        model = CommodityModel()
        model.name = input("请输入学生姓名:")
        model.price = int(input("请输入学生年龄:"))
        self.controller.add_commodity(model)
        print("添加成功")


class CommodityController:
    def add_commodity(self, new):
        """
            添加商品信息(设置商品编号,追加到列表中)
        :param new: CommodityModel类型,在view中录入的商品信息
        """
        pass


view = CommodityView()
while True:
    view.display_menu()
    view.select_menu()
