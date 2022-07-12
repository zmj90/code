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

    def __str__(self):
        return f"{self.name}的编号是{self.cid},单价是{self.price}"

    def __eq__(self, other):
        return self.cid == other


class CommodityView:
    """
        界面视图:负责处理商品信息的输入/输出逻辑
    """

    def __init__(self):
        self.__controller = CommodityController()

    def __display_menu(self):
        """
            显示菜单
        """
        print("1键录入商品信息")
        print("2键显示商品信息")
        print("3键删除商品信息")
        print("4键修改商品信息")

    def __select_menu(self):
        """
            选择菜单
        """
        item = input("请输入选项:")
        if item == "1":
            # 难点1:本类多个方法互相调用
            # 通过self调用
            self.__input_commodity()
        elif item == "2":
            # 难点1:本类多个方法互相调用
            # 通过self调用
            self.__display_commoditys()
        elif item == "3":
            self.__delete_commodity()
        elif item == "4":
            self.__modify_commodity()

    def __input_commodity(self):
        """
            录入商品信息
        """
        # 难点2:跨类调用方式1(直接创建对象)
        model = CommodityModel()
        model.name = input("请输入商品名称:")
        model.price = int(input("请输入商品单价:"))
        self.__controller.add_commodity(model)
        print("添加成功")

    def __display_commoditys(self):
        for item in self.__controller.list_commodity:
            # print(f"{item.name}的编号是{item.cid},单价是{item.price}")
            print(item)

    def __delete_commodity(self):
        cid = int(input("请输入商品编号："))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_commodity(self):
        model = CommodityModel()
        model.cid = int(input("请输入商品编号:"))
        model.name = input("请输入商品名称:")
        model.price = int(input("请输入商品单价:"))
        if self.__controller.update_commodity(model):
            print("修改成功")
        else:
            print("修改失败")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()


class CommodityController:
    def __init__(self):
        self.__start_id = 1001
        self.list_commodity = []

    def add_commodity(self, new):
        """
            添加商品信息(设置商品编号,追加到列表中)
        :param new: CommodityModel类型,在view中录入的商品信息
        """
        new.cid = self.__start_id
        self.list_commodity.append(new)

    def remove_commodity(self, cid):
        """
            在列表中移除学生信息
        :param cid: int类型,学生编号
        :return: bool类型,是否成功移除
        """
        if cid in self.list_commodity:
            self.list_commodity.remove(cid)
            return True
        return False

    def update_commodity(self, model):
        """

        :param model:
        :return:
        """
        for item in self.list_commodity:
            if item.cid == model.cid:
                item.__dict__ = model.__dict__
                return True
        return False


view = CommodityView()
view.main()
